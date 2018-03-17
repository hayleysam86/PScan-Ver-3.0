import os
import socket
import sys
import pip._vendor.ipaddress

targetIP = raw_input('[-] Enter Target website/IP: ')
targetIPa = socket.gethostbyname(targetIP)
targetIPn = pip._vendor.ipaddress.ip_address(unicode(targetIPa))
#targetPort = input('[-] Enter Target port: ')
#SetTimeOut = 0
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
		reply = soc.recv(1024)
		print("[-] Recieved: " + str(reply) + " from " + str(targetIPa) + " on port: " + str(targetPort) + "\n")
	except (Exception) as e:
		print("[-] Error with target: " + targetIPa + " : " + str(e) + " on port: " + str(i))

i = 1
while (i < 2000):
	Connect(targetIPa, i, SetTimeOut)
	i = i + 1



#Connect((targetIPa, i, SetTimeOut))
#print(str(reply))