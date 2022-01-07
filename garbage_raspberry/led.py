import time
import RPi.GPIO as GPIO
import pins


def led_on():
    GPIO.output(pins.LED_PIN, GPIO.HIGH)


def led_off():
    GPIO.output(pins.LED_PIN, GPIO.LOW)


def blink(blinks=3, sleeps=0.3):
    for i in range(blinks):
        led_on()
        time.sleep(sleeps)
        led_off()
        time.sleep(sleeps)


def await_blinking():
    for i in range(30):
        led_on()
        time.sleep(0.8)
        led_off()
        time.sleep(0.8)
        blink(blinks=2, sleeps=0.2)
