import socket
import RPi.GPIO as GPIO
import time
import sys

## 31: arriere
## 33: avant
## 35: gauche
## 37: droite

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 666))

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)

socket.listen(5)
client, address = socket.accept()
print("{} connected" + format( address ))

while True:
	response = client.recv(1024)

	if response == 'q':
		sys.exit()
	elif response == 'recule':
		print("recule")
		GPIO.output(31,GPIO.HIGH)
	elif response == 'avance':
		print("avance")
		GPIO.output(33,GPIO.HIGH)
	elif response == 'gauche':
		print("gauche")
		GPIO.output(35,GPIO.HIGH)
	elif response == 'droite':
		print("droite")
		GPIO.output(37,GPIO.HIGH)
	elif response == 'fin recule':
		print("fin recule")
		GPIO.output(31,GPIO.LOW)
	elif response == 'fin avance':
		print("fin avance")
		GPIO.output(33,GPIO.LOW)
	elif response == 'fin gauche':
		print("fin gauche")
		GPIO.output(35,GPIO.LOW)
	elif response == 'fin droite':
		print("fin droite")
		GPIO.output(37,GPIO.LOW)
	elif response == 'cleanup':
		print("cleanup")
		GPIO.cleanup()
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(31,GPIO.OUT)
		GPIO.setup(33,GPIO.OUT)
		GPIO.setup(35,GPIO.OUT)
		GPIO.setup(37,GPIO.OUT)

print("Close") 
client.close()
stock.close()
