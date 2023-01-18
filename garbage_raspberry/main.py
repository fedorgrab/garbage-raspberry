import time

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
from picamera import PiCamera

import constants
import hardware
import led
import pins
import rp_camera
import server
import servo

if __name__ == "__main__":
    print("Ready to work")
    hardware.setup()
    rp_camera.camera_stream()
