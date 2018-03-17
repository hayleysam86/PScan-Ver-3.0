import socket
import time

host "www.google.com"

def __Connect__():
	soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 80
	soc.bind((host, port))
	soc.listen(5)

	while True:
		soc.addr = soc.accept()
		print("recieved: " + ")
