#import required functions.
import os, socket, sys, argparse, time
from threading import Thread

Logging_Enabled = bool
Logging_Enabled = True

#deafult ports to check
__Default_Ports = [13,15,21,22,25,53,80,123,125,110,135,137,139,443,1433,1434,8080]

#Connection Function
def __Connect(__Target, __Target_Port, __SetTimeOut):
	Logging_Enabled = bool
	Logging_Enabled = True
	try:
		socket.setdefaulttimeout(__SetTimeOut)
		__Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		__Soc.connect((__Target_Resolve, __Target_Port))
		__Soc.send(args.__Junk)
		__Reply = __Soc.recv(1024)
		__Soc.close()
		print("[-] Recieved " + str(__Reply) + " from " + str(__Target_Resolve) + " / " + str(__Target) + " on port " + str(__Target_Port))
		if(str(args.Logging_Enabled) == 'False'):
			__WriteLog("[-] Recieved " + str(__Reply) + " \n\tfrom " + str(__Target_Resolve) + " / " + str(__Target) + " on port " + str(__Target_Port))
	except (Exception) as e:
		print("[-] Error: " + args.__Target + " on port " + str(__Target_Port) + " : " + str(e))
		if(str(args.Logging_Enabled) == 'False'):
			__WriteLog("[-] Error: " + args.__Target + " on port " + str(__Target_Port) + " : " + str(e))

def __WriteLog(__Data):
	LogOpen = open("log.txt", "a")
	LogOpen.write(str(__Data) + "\n")
	LogOpen.close()

__Target = None
Logging_Enabled = bool
Logging_Enabled = True
Port_Specific = None

###Parse user defined arguments
__Parser = argparse.ArgumentParser()
__Parser.add_argument('-l', help='Enable logging to the file log.txt in current working directory', action='store_false', dest='Logging_Enabled')
__Parser.add_argument('-p', help='Specify what ports to scan. Defaults to a specific list of ports if flag isnt used.', action='store', dest='Port_Specific', nargs='*',type=int)
__Parser.add_argument('-j', help='Junk data to be sent to each port', action='store', dest='__Junk', default='\x00\x00\x00\x00')
__Parser.add_argument('-t', help='Add a target from the command line', action='store', dest='__Target')
args = __Parser.parse_args()


print(str(args.__Target))
#ask user for targetbto scan.
if ( str(args.__Target) == 'None'):
	__Target = raw_input('[-] Enter target IP/web address: ')
	__Target_Resolve = socket.gethostbyname(__Target)
	#print initial data
	print("\n[-] Resolved " + str(args.__Target) + " to IP address: " + str(__Target_Resolve))

#set timeout for each connection
__SetTimeOut = input('[-] Enter timeout in sec: ')

__Junk = '\x00\x00\x00\x00'

if(str(args.Logging_Enabled) == 'False'):
	__WriteLog("PScan.py initiated at " + time.asctime())

###Scan using the default ports listed in __Default_Ports
if (args.Port_Specific == None):
	i = 1
	while (i < len(__Default_Ports)):
		T = Thread(__Connect(args.__Target, __Default_Ports[i], __SetTimeOut))
		T.start()
		i = i + 1

###Scan using user given parameters this runs through all user given parameters
###Used if the user supplys more than one argument
elif ( args.Port_Specific != None):
	i = 0
	if ( len(args.Port_Specific) >= 1 ):
		while ( i < len(args.Port_Specific)):
			T = Thread(__Connect(args.__Target, int(args.Port_Specific[i]), __SetTimeOut))
			T.start()
			i = i + 1

###Scan using user specific variables
###Used if only one option is supplied by the user
	elif ( len(args.Port_Specific) == 0 ):
		i = 1
		T = Thread(__Connect(args.__Target, int(arg.Port_Specific), __SetTimeOut))
		T.start
