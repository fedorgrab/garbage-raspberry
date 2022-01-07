from adafruit_servokit import ServoKit
from picamera import PiCamera
import RPi.GPIO as GPIO
import servo
import constants
import pins


servo_kit = ServoKit(channels=16)
camera = PiCamera()


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pins.LED_PIN, GPIO.OUT)
    camera.resolution = constants.IMG_SIZE
    camera.awb_mode = "auto"
