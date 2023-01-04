import typing as t
import time
import io
from PIL import Image
from picamera.array import PiRGBArray
import imagehash

import constants
import server
import led
import servo
import hardware


def camera_on_action(images, start_time) -> str:
    predicted_class = server.send_images_and_predict(images)
    print(f"=== Finished Processing: {str(time.time() - start_time)[:6]} s. Predicted class: {predicted_class}")
    if predicted_class == "other":
        led.blink()
    elif predicted_class == "service_gesture":
        led.await_blinking()
    else:
        bin_type = constants.CLASS_TO_BIN_MAP[predicted_class]
        bin_door = hardware.servo_kit.servo[bin_type]
        servo.open_door(bin_door)
        time.sleep(5)
        servo.close_door(bin_door)
        
    return predicted_class


def camera_stream() -> None:
    k = 0
    time.sleep(1)
    stream = io.BytesIO()
    raw_capture = PiRGBArray(hardware.camera, size=constants.IMG_SIZE)
    prev_image = None

    print("Start")
    on_camera_images = []
    object_is_close = False
    start_time = None

    for frame in hardware.camera.capture_continuous(
        raw_capture, "bgr", use_video_port=True
    ):
        img_arr = frame.array
        img = Image.fromarray(img_arr)
        raw_capture.truncate(0)

        if img_arr.mean() < 10:
            print("Black Image")
            prev_image = None
            object_is_close = False
            on_camera_images = []
            k = 0
            continue


        if prev_image is None:
            prev_image = img
            continue
        
        prev_image_hash = imagehash.average_hash(prev_image)
        curr_image_hash = imagehash.average_hash(img)
        hash_diff = prev_image_hash - curr_image_hash

        if abs(hash_diff) > 3 or object_is_close:
            if k == 0:
                print("Scanning Object")
                start_time = time.time()
                led.led_on()
                time.sleep(0.6)
                object_is_close = True
            elif 0 < k < constants.NUMBER_OF_IMAGES_TO_PROCESS:
                on_camera_images.append(img)
            elif k >= constants.NUMBER_OF_IMAGES_TO_PROCESS:
                led.led_off()
                predicted_class = camera_on_action(on_camera_images, start_time=start_time)
                prev_image = None
                object_is_close = False
                on_camera_images = []
                k = 0
                continue

            k += 1
            continue

        prev_image = img
        k = 0
