import os
import sys
import socket
import pip._vendor.ipaddress

global targetIP
global targetIP2
global targetPort

def IP_convert(targetIP):
	global targetIPa

	targetIP2 = socket.gethostbyname(targetIP)
	targetIPa = pip._vendor.ipaddress.ip_address(unicode(targetIP2))
	return targetIPa, targetIP2, targetIP

def main():
	targetIP = raw_input('Enter target website/IP: ')
	targetPort = raw_input('Enter target port: ')
	IP_convert(targetIP)
	printStuff(targetIPa)
	return targetIP, targetPort

def printStuff(targetIPa):
	global targetIP
	print("\nLocating " + targetIP + ". Resolved to IP address: " + targetIPa)

if __name__ == '__main__':
	main()

