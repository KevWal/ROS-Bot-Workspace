#!/usr/bin/python3

from gpiozero import DigitalInputDevice
from time import sleep

from gpiozero import Button

SAMPLETIME = 2

class Encoder(object):
    def __init__(self, pin):
        self._value = 0
        self._encoder = DigitalInputDevice(pin, pull_up=True)
        self._encoder.when_activated = self._increment
        self._encoder.when_deactivated = self._increment
        print("Init")

    def reset(self):
        self._value = 0

    def _increment(self):
        self._value += 1
        print("Inc")

    @property
    def value(self):
        return self._value


button = Button(23, pull_up=True)
button.wait_for_press()
print("23 was pressed!")
button.wait_for_release()
print("23 was released!")
button.close()

button = Button(24, pull_up=True)
button.wait_for_press()
print("24 was pressed!")
button.wait_for_release()
print("24 was released!")
button.close()

e1 = Encoder(23)
e2 = Encoder(24)

while True:
    print("e1 {} e2 {}".format(e1.value, e2.value))
    sleep(SAMPLETIME)



