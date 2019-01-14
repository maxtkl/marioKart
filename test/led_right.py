#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

LedPinR = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPinR, GPIO.OUT)
GPIO.output(LedPinR, GPIO.LOW)
time.sleep(5)
GPIO.output(LedPinR, GPIO.HIGH)

GPIO.cleanup()
