#!/usr/bin/env python
# coding: utf-8

import socket
import json
from pynput import keyboard
from struct import pack
from struct import unpack
from struct import calcsize as sizeof
from threading import Thread
import time
import sys

#server = "192.168.1.1"
#port = 1337
server = "192.168.1.1"
port = 1337

other_player = ['192.168.1.100','192.168.1.101','192.168.1.102','192.168.1.103','192.168.1.104','192.168.1.105','192.168.1.107','192.168.1.108']
CONNECT_TO_CAR = 1
MOVE_CAR = 2
GET_MALUS = 3
SEND_MALUS = 4
nb_malus = 0

# Cree un paquet avec le code du type de message
def create_packet(op_code, data):
	return pack("!I{}s".format(len(data)), op_code, data.encode())

# Extrait le code du type de message ainsi que les donnees du paquet
def process_packet(packet):
	return unpack("!I{}s".format(len(packet)-sizeof("!I")), packet)

def on_press(key):
	try:
		global nb_malus
		if key == keyboard.Key.up:
			socket.send(create_packet(MOVE_CAR,"forward"))
		if key == keyboard.Key.down:
			socket.send(create_packet(MOVE_CAR,"backward"))
		if key == keyboard.Key.left:
			socket.send(create_packet(MOVE_CAR,"left"))
		if key == keyboard.Key.right:
			socket.send(create_packet(MOVE_CAR,"right"))
		if key == keyboard.KeyCode.from_char('a') and nb_malus > 0:
			socket.send(create_packet(MOVE_CAR,"malus"))
			socket.send(create_packet(SEND_MALUS,other_player[0]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('z') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[1]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('e') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[2]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('r') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[3]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('t') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[4]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('y') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[5]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('u') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[6]))
			nb_malus -= 1
		if key == keyboard.KeyCode.from_char('i') and nb_malus > 0:
			socket.send(create_packet(SEND_MALUS,other_player[7]))
			nb_malus -= 1
		if key == keyboard.Key.space:
			socket.send(create_packet(MOVE_CAR,"cleanup"))
	except AttributeError:
		print('special key {0} pressed'.format(key))

def on_release(key):
	if key == keyboard.Key.up:
		print("end avant")
		socket.send(create_packet(2,"end forward"))
	if key == keyboard.Key.down:
		print("end arriere")
		socket.send(create_packet(2,"end backward"))
	if key == keyboard.Key.left:
		print("end left")
		socket.send(create_packet(2,"end left"))
	if key == keyboard.Key.right:
		print("end right")
		socket.send(create_packet(2,"end right"))
	if key == keyboard.Key.esc:
		return False

def malus_obtained():

	global nb_malus

	while True:

		packet = socket.recv(1024)
		code, unpacked = process_packet(packet)
		if code == GET_MALUS:
			print("malus_obtained")
			nb_malus += 1



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((server, port))
print("Connection on " + format(port))

socket.send(create_packet(CONNECT_TO_CAR,json.dumps({"ip": "192.168.1.106","port": 1989})))

thread = Thread(target = malus_obtained)
thread.start()

# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

print("Close")
socket.close()
