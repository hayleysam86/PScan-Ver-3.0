import os
import socket
import sys
import pip._vendor.ipaddress
from threading import Thread
import optparse

defaultPorts = [13,15,21,22,23,80,123,125,8080,9600,53,25,443,110,135,137,139,1433,1434]

targetIP = raw_input('[-] Enter Target website/IP: ')
targetIPa = socket.gethostbyname(targetIP)
targetIPn = pip._vendor.ipaddress.ip_address(unicode(targetIPa))
#targetPort = input('[-] Enter Target port: ')
SetTimeOut = input('[-] Enter Timeout in seconds: ')

print("\n[-] Locating " + targetIP + ". Resolved to: " + str(targetIPn))
#print("\ntargetIPn: " + str(targetIPn) + "\n")
#print("targetIPa: " + str(targetIPa))
#print("targetIP: " + str(targetIP))
#print("tuple: " + str(tuple(targetIPa)))

def Connect(targetIPa, targetPort, SetTimeOut):
	try:
		socket.setdefaulttimeout(SetTimeOut)
		soc = socket.socket()
		soc.connect((targetIPa, targetPort))
		soc.send('\x00\x00\x00')
		reply = soc.recv(1024)
		soc.close()
		print("[-] Recieved: " + str(reply) + " from " + str(targetIPa) + str(targetIP) +" on port: " + str(targetPort) + "\n")
	except (Exception) as e:
		print("[-] Error with target: " + targetIPa + " : " + str(e) + " on port: " + str(defaultPorts[i]))

i = 1
while (i < len(defaultPorts)):
	t = Thread(Connect(targetIPa, defaultPorts[i], SetTimeOut))
	t.start()
	i = i + 1