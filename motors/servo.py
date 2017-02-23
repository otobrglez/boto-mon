#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from time import sleep
import RPi.GPIO as GPIO


class Servo:
    def __init__(self, gpioPin, initDegrees):
        # GPIO.setmode(GPIO.BCM)  # pin numbering scheme that uses GPIO numbers
        # GPIO.setwarnings(False)
        GPIO.setup(gpioPin, GPIO.OUT)  # set GPIO 25 as output
        self.servo = GPIO.PWM(gpioPin, 50)  # instantiate PWM output to GPIO `pin` @ 50Hz

        self.degree_sign = u'\N{DEGREE SIGN}'  # unicode for the degree symbol
        self.degree_text = "deg"  # unicode for the degree symbol
        self.dc_min = 2.1  # the min duty cycle corresponding to 210deg rotation
        self.dc_max = 12.3  # the max duty cycle corresponding to 0deg rotation

        #self.deg_min = 0
        #self.deg_mid = 105
        #self.deg_max = 210

        self.deg_min = 0
        self.deg_mid = 105
        self.deg_max = 360

        # start at the provided rotation
        self._initRotateTo(initDegrees)

    def _degreesToDutyCycle(self, degrees):
        # assert proper use
        assert isinstance(degrees, int)
        assert (self.deg_min <= degrees <= self.deg_max)
        # convert degrees to fraction out of 210
        rotation = degrees / 210.0
        # convert fraction to the duty cycle from that corresponding to 0deg
        # looks odd since max_dc corresponds to min degree position,
        # and vice-versa
        dc_from_max = ((self.dc_max - self.dc_min) * rotation)
        # return the dc for the deg position
        return self.dc_max - dc_from_max

    def _initRotateTo(self, degrees):
        duty_cycle = self._degreesToDutyCycle(degrees)
        self.servo.start(duty_cycle)  # start at init degree position
        print("Servo: Rotated to " + str(degrees) + self.degree_text)

    def rotateTo(self, degrees):
        # convert to the duty cycle
        duty_cycle = self._degreesToDutyCycle(degrees)
        # adjust duty cycle
        self.servo.ChangeDutyCycle(duty_cycle)
        print("Servo: Rotated to " + str(degrees) + self.degree_text)

    def test(self):
        positions = [105, 210, 105, 0]

        for position in positions:
            self.rotateTo(position)
            time.sleep(1)  # wait until rotation is finished

    def __exit__(self, exc_type, exc, traceback):
        print("Servo: Exiting, cleaning up")
        self.servo.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    try:
        s = Servo(7, 0)
        while True:
            degree = input("Rotate to degrees : ")
            print("Trying to rotate to {}".format(degree))

            s.rotateTo(int(degree))
            sleep(5)

    except KeyboardInterrupt:
        print("Exit.")

    #sleep(3)
    #s.rotateTo(90)
    #sleep(3)
    #s.rotateTo(180)
    #sleep(3)
    #s.rotateTo(350)
    #sleep(0)
    #s.rotateTo(0)
