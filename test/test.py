import RPi.GPIO as GPIO
import time
import sys
## 31: arriere
## 33: avant
## 35: gauche
## 37: droite

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.output(13,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
print "Arriere ..."
GPIO.output(31,GPIO.HIGH)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)
time.sleep(1)
print "Avant..."
GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.HIGH)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)
time.sleep(1)
print "Gauche ..."
GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.HIGH)
GPIO.output(37,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
time.sleep(1)
print "Droite ..."
GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.HIGH)
GPIO.output(13,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
time.sleep(1)
print "Test slow"
GPIO.output(15,GPIO.HIGH)
GPIO.output(37,GPIO.LOW)
p = GPIO.PWM(33,50)
p.start(25)
p.ChangeDutyCycle(60)
time.sleep(1)
print "Change speed"
p.ChangeDutyCycle(25)
time.sleep(2)
p.stop()

print "Stop"
GPIO.output(31,GPIO.LOW)
GPIO.output(33,GPIO.LOW)
GPIO.output(35,GPIO.LOW)
GPIO.output(37,GPIO.LOW)
time.sleep(1)

GPIO.cleanup()