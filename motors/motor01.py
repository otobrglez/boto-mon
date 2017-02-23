from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)


p = GPIO.PWM(7, 50)
p.start(5)  # 7.5

k = GPIO.PWM(11, 50)
k.start(5)


def changeSleep(p, value, delay):
    print("Setting duty cycle to {} and sleeping {}".format(value, delay))
    p.ChangeDutyCycle(value)
    sleep(delay)


try:
    while True:
        #        GPIO.output(7, 1)
        ##        time.sleep(0.0015)
        #        GPIO.output(7,0)
        #        time.sleep(2)

        changeSleep(k, 3, 0.5)
        changeSleep(p, 3, 0.5)

        changeSleep(p, 4, 0.5)
        changeSleep(k, 4, 0.5)

        changeSleep(p, 5, 0.5)
        changeSleep(k, 5, 0.5)

        changeSleep(p, 6, 0.5)
        changeSleep(k, 6, 0.5)

        changeSleep(p, 7, 0.5)
        changeSleep(k, 7, 0.5)

        changeSleep(p, 8, 0.5)
        changeSleep(k, 8, 0.5)

        changeSleep(p, 9, 0.5)
        changeSleep(k, 9, 0.5)

        changeSleep(p, 10, 0.5)
        changeSleep(k, 10, 0.5)


        # p.ChangeDutyCycle(8)  # 180
        # time.sleep(2)

except KeyboardInterrupt:
    p.stop()
    k.stop()
    GPIO.cleanup()
