import socket
import home_network
import json
import time

tab_ip_port = []
tab_conn = {}

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.bind(('', 15555))
print("server testone started")

socket1.listen(1)
client, address = socket1.accept()
print("{} connected".format( address ))

while True:
	time.sleep(3)
	
	response = client.recv(1048)
	(code, data) = home_network.process_packet(response)
	try:
		if code == home_network.CONNECT_TO_CAR:
			data = json.loads(data.decode())
			if (data['ip'],data['port']) not in tab_ip_port:
				server_to_car = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				server_to_car.connect((data['ip'], data['port']))
				print("Connected to car on address: {} on port: {}".format(data['ip'],data['port']))
				tab_ip_port.append((data['ip'],data['port']))
				tab_conn[client] = server_to_car
				print(server_to_car)
			else:
				print("La voiture de l'adresse {} est déjà connectée à ce port".format(data['ip']))
		elif code == home_network.MOVE_CAR:
			tab_conn[client].send(data)
			print(data)
		elif code == home_network.GET_MALUS:
			tab_conn[client].send(data)
			print(data) 
		elif code == home_network.SEND_MALUS:
			tab_conn[client].send(data)
			print(data)
	except:
		print("Une erreur est arrivée")

print("Close testone")
client.close()
stock.close()
