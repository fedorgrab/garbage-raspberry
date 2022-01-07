import time
from adafruit_servokit import ServoKit
from picamera import PiCamera
import RPi.GPIO as GPIO
import rp_camera
import servo
import constants
import server
import pins
import led
import hardware


if __name__ == "__main__":
    print("Ready to work")
    hardware.setup()
    rp_camera.camera_stream()
