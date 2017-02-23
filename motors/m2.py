import RPi.GPIO as GPIO
from time import sleep
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

p = GPIO.PWM(7, 50)

p.start(7)
sleep(1)

p.ChangeDutyCycle(8)
sleep(1)

p.ChangeDutyCycle(8)
sleep(1)

p.ChangeDutyCycle(8)
sleep(1)

p.ChangeDutyCycle(9)
sleep(1)

p.ChangeDutyCycle(8)
sleep(1)

p.stop()

GPIO.cleanup()
# pwm.ChangeDutyCycle(7.5)
