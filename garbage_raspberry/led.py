import time

from hardware import led_channel


def led_on():
    led_channel.duty_cycle = 0xFFFF


def led_off():
    led_channel.duty_cycle = 0


def blink(blinks=3, sleeps=0.3):
    for i in range(blinks):
        led_on()
        time.sleep(sleeps)
        led_off()
        time.sleep(sleeps)


def start_blink():
    blink(blinks=2, sleeps=0.2)


def await_blinking():
    for i in range(30):
        led_on()
        time.sleep(0.8)
        led_off()
        time.sleep(0.8)
        blink(blinks=2, sleeps=0.2)
