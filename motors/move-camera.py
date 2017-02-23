#!/usr/bin/env python
from sys import stdin
from time import sleep
import tty, termios, sys
import RPi.GPIO as GPIO


def getchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def change_sleep(pin, value, delay=None):
    print("Setting duty cycle to {} and sleeping {}".format(value, delay))
    pin.ChangeDutyCycle(value)
    if delay is not None: sleep(delay)


if __name__ == '__main__':
    P_START, K_START = 5, 5

    # Setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)

    print("Getting ready,...")
    p = GPIO.PWM(7, 70)
    p.start(P_START)

    k = GPIO.PWM(11, 70)
    k.start(K_START)
    sleep(3)
    print("Ready.")

    MINI_STEP = 0.2

    try:
        v_pos = P_START
        h_pos = K_START
        while True:

            print("==>")
            ch = getchar()
            if ch is 'q': raise KeyboardInterrupt()

            if ch is 'a':  # left
                print("left")
                h_pos += MINI_STEP
                change_sleep(p, h_pos)
            elif ch is 'd': # right
                print("right")
                h_pos -= MINI_STEP
                change_sleep(p, h_pos)
            elif ch is 'w': # up
                print("up")
                v_pos += MINI_STEP
                change_sleep(k, v_pos)
            elif ch is 's': # down
                v_pos -= MINI_STEP
                change_sleep(k, v_pos)







    except KeyboardInterrupt:
        GPIO.cleanup()
