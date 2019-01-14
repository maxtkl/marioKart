#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import sys

LedPinG = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPinG, GPIO.OUT)
GPIO.output(LedPinG, GPIO.LOW)
time.sleep(5)
GPIO.output(LedPinG, GPIO.HIGH)

GPIO.cleanup()
