import socket;
import os;
import pprint;
import pip._vendor.ipaddress;

port = 80
Junk = 'HTTP/1.0 GET OK\r\n'
##IA = "asus"
IP = "192.168.1.1"
##socket.gethostbyname(IA)
socket.setdefaulttimeout(10)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##print(IP)
soc.bind((pip._vendor.ipaddress(IP), port))
##soc.connect((IP,800))
##soc.send(Junk)
##soc.listen()
##RP = soc.recv(1024)
##print("Pinging " + str(IP) + " Resolved from: " + str(IA) + " Recieved: " + str(RP))