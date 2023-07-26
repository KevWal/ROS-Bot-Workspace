#!/usr/bin/python3

from time import time, sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

v23_value = 0
v24_value = 0

def v23_change(channel):
    global v23_value
    v23_value += 1

def v24_change(channel):
    global v24_value
    v24_value += 1

GPIO.add_event_detect(23, GPIO.BOTH, callback=v23_change, bouncetime=1)
GPIO.add_event_detect(24, GPIO.BOTH, callback=v24_change, bouncetime=1)

while True:
    print("e1 {} e2 {}".format(v23_value, v24_value))
    sleep(2)
