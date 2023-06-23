#!/usr/bin/python3

from RPi import GPIO
from time import sleep

class Encoder(object):
    def __init__(self, pin):
        self._value = 0

        # setup gpio to call increment on each when_activated
        GPIO.setup(pin, GPIO.IN) # pull_up_down=GPIO.PUD_DOWN
        GPIO.add_event_detect(pin, GPIO.BOTH, callback=self._increment, bouncetime=1)

    def reset(self):
        self._value = 0

    def _increment(self, channel):
        self._value += 1

    @property
    def value(self):
        return self._value

GPIO.setmode(GPIO.BCM)

SAMPLETIME = 1

e1 = Encoder(23)
e2 = Encoder(24)

#find a sample rate
while True:
    print("e1 {} e2 {}".format(e1.value, e2.value))
    sleep(SAMPLETIME)
