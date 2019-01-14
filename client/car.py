import socket
import RPi.GPIO as GPIO
import time
import sys

pin_led_left = 13
pin_led_right = 15
pin_avance = 33
pin_recule = 31
pin_left = 35
pin_right = 37

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 1989))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_recule,GPIO.OUT)
GPIO.setup(pin_avance,GPIO.OUT)
GPIO.setup(pin_left,GPIO.OUT)
GPIO.setup(pin_right,GPIO.OUT)
GPIO.setup(pin_led_left,GPIO.OUT)
GPIO.setup(pin_led_right,GPIO.OUT)
GPIO.output(pin_led_left,GPIO.HIGH)
GPIO.output(pin_led_right,GPIO.HIGH)

socket.listen(5)
client, address = socket.accept()
print("{} connected" + format( address ))

while True:
	response = client.recv(1024)

	if response == 'q':
		sys.exit()
	elif response == 'backward':
		GPIO.output(pin_recule,GPIO.HIGH)
	elif response == 'forward':
		GPIO.output(pin_avance,GPIO.HIGH)
	elif response == 'left':
		GPIO.output(pin_left,GPIO.HIGH)
		GPIO.output(pin_led_left,GPIO.LOW)
	elif response == 'right':
		GPIO.output(pin_right,GPIO.HIGH)
		GPIO.output(pin_led_right,GPIO.LOW)
	elif response == 'end backward':
		GPIO.output(pin_recule,GPIO.LOW)
	elif response == 'end forward':
		GPIO.output(pin_avance,GPIO.LOW)
	elif response == 'end left':
		GPIO.output(pin_left,GPIO.LOW)
		GPIO.output(pin_led_left,GPIO.HIGH)
	elif response == 'end right':
		GPIO.output(pin_right,GPIO.LOW)
		GPIO.output(pin_led_right,GPIO.HIGH)
	elif response == 'cleanup':
		GPIO.cleanup()
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin_recule,GPIO.OUT)
		GPIO.setup(pin_avance,GPIO.OUT)
		GPIO.setup(pin_left,GPIO.OUT)
		GPIO.setup(pin_right,GPIO.OUT)
		GPIO.setup(pin_led_left,GPIO.OUT)
		GPIO.setup(pin_led_right,GPIO.OUT)
		GPIO.output(pin_led_left,GPIO.HIGH)
		GPIO.output(pin_led_right,GPIO.HIGH)

print("Close")
client.close()
stock.close()
