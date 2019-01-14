import RPi.GPIO as GPIO
import time
import sys
import pygame

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

pygame.init()

pygame.display.set_mode((100, 100))

###############################   step 1    #############################

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
			print("exit")
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				GPIO.output(31,GPIO.HIGH)
				print("fleche bas ok")
			elif event.key == pygame.K_UP:
				GPIO.output(33,GPIO.HIGH)
				print("fleche haut ok")
			elif event.key == pygame.K_LEFT:
				GPIO.output(35,GPIO.HIGH)
				GPIO.output(13,GPIO.LOW)
				print("fleche gauche ok")
			elif event.key == pygame.K_RIGHT:
				GPIO.output(37,GPIO.HIGH)
				GPIO.output(15,GPIO.LOW)
				print("fleche droite ok")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				GPIO.output(31,GPIO.LOW)
				print("fleche bas pas ok")
			elif event.key == pygame.K_UP:
				GPIO.output(33,GPIO.LOW)
				print("fleche haut pas ok")
			elif event.key == pygame.K_LEFT:
				GPIO.output(35,GPIO.LOW)
				GPIO.output(13,GPIO.HIGH)
				print("fleche gauche pas ok")
			elif event.key == pygame.K_RIGHT:
				GPIO.output(37,GPIO.LOW)
				GPIO.output(15,GPIO.HIGH)
				print("fleche droite pas ok")
		else:
			pass


GPIO.cleanup()
