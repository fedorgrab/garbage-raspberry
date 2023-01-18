import adafruit_pca9685
import board
import busio
import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
from picamera import PiCamera

import constants
import pins
import servo

servo_kit = ServoKit(channels=16)
i2c = busio.I2C(board.SCL, board.SDA)
pca = adafruit_pca9685.PCA9685(i2c)
pca.frequency = 60
led_channel = pca.channels[pins.LED_PCA_CHANNEL]
camera = PiCamera()


def setup():
    GPIO.setmode(GPIO.BCM)
    camera.resolution = constants.IMG_SIZE
    camera.awb_mode = "auto"
