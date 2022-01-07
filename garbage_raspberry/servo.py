import time


OPEN_DOOR_ANGLE = 39
CLOSE_DOOR_ANGLE = 3


def open_door(servo):
    for i in range(CLOSE_DOOR_ANGLE, OPEN_DOOR_ANGLE, 8):
        servo.angle = i
        time.sleep(0.1)
    servo.angle = OPEN_DOOR_ANGLE


def close_door(servo):
    for i in range(OPEN_DOOR_ANGLE, CLOSE_DOOR_ANGLE, -3):
        servo.angle = i
        multiplicative_factor = i if i > 25 else 25
        time.sleep(4 * multiplicative_factor ** -1)

    servo.angle = CLOSE_DOOR_ANGLE
