import socket
from struct import pack
import json
import time

hote = "localhost"
port = 15555

CONNECT_TO_CAR = 1
MOVE_CAR = 2
GET_MALUS = 3

# Cree un paquet avec le code du type de message
def create_packet(op_code, data):
	return pack("!I{}s".format(len(data)), op_code, data.encode())


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

socket.send(create_packet(CONNECT_TO_CAR,json.dumps({"ip": "localhost","port": 1989})))


time.sleep(3)
while True:
	socket.send(create_packet(MOVE_CAR,"avance"))
	time.sleep(2)
	print("sesses")
	socket.send(create_packet(GET_MALUS,"malus"))

print("Close")
socket.close()