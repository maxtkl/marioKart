import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 1989))

socket.listen(5)
client, address = socket.accept()
print("{} connected".format( address ))
	
while True:
	
	response = client.recv(255)
	if response != '':
		print(response)

print("Close")
client.close()
stock.close()