import pip._vendor.ipaddress;
import socket;
from socket import *
import os;
import pprint;
import threading

TargetIPAddressAfter = ''
TargetPortAfter = 0

def __NewFunctionm__():
	TargetIPAddress = raw_input('Enter Target IP Address: ')
	TargetIPAddressAfter = pip._vendor.ipaddress.ip_network(unicode(TargetIPAddress))
	return TargetIPAddressAfter

def __NextFunction__():
	TargetPort = int(input('Enter Target Port: '))
	TargetPortAfter = TargetPort
	return TargetPortAfter

def __Connect__(TargetIPAddressAfter, TargetPortAfter):
	soc = socket(AF_INET, SOCK_STREAM)
	soc.connect((TargetIPAddressAfter, TargetPortAfter))
	reply = soc.recv(1024)
	return reply

def __main__():
	__NewFunctionm__()
	__NextFunction__()
	__Connect__(TargetIPAddressAfter, TargetPortAfter)

	print(reply)
	return

if __name__ == "__main__":
	__main__()