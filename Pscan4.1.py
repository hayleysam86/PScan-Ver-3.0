import os, sys, time, socket, argparse
from threading import Thread

def __Load_Variables():
	__Logging = True
	__Target = None
	__Default_Ports = [13,15,21,22,25,53,80,123,125,110,135,137,139,443,1433,1434,8080]
	__Port_Specific = None
	__Junk = "test"
	__SetTimeOut = None
	return __Logging, __Target, __Default_Ports, __Port_Specific, __Junk, __SetTimeOut

def __Header():
	print('')
	print(' *******  ******  ******  *****     **   **        ')
	print(' **   **  **      **   *  **  **    ***  **      ')
	print(' *******  ******  **      ******    **** **             ')
	print(' **           **  **   *  **   **   ** ****          ')         
	print(' **       ******  ******  **    **  **   ** Ver 4.1               \n')
	print('[-] Port Scanning softare. Developed by otac0n. Licsense under GPL 3.0\n')

__Header()

def main():

	__Variables = __Load_Variables()

	__Parser = argparse.ArgumentParser()
	__Parser.add_argument('-l', help='Enable logging to log.txt', action='store_false', dest='__Logging', default='True')
	__Parser.add_argument('-p', help='Supply port to be scanned, Use 0 to select default ports', action='store', dest='__Port_Specific', nargs='*', type=int, default=0, required='True')
	__Parser.add_argument('-j', help='Supply Junk data to be sent to the server', action='store', dest='__Junk', default='test')
	__Parser.add_argument('-t', help='Supply Target in the CLI.', action='store', dest='__Target')
	Args = __Parser.parse_args()

	__Logging = Args.__Logging
	__Target = Args.__Target
	__Junk = Args.__Junk
	__Port_Specific = Args.__Port_Specific

	return __Variables, __Logging, __Target, __Junk, __Port_Specific

main()

def __Logging_Enabled():
	__Vars = main()
	if (str(__Vars[1]) == 'False'):
		__Logging = __Vars[1]
		print('[-] Logging Enabled')
		return __Logging
	elif(str(__Vars[1]) != 'False'):
		__Logging = __Vars[1]
		print('[-] Logging disabled')
		return __Logging 
	return __Logging 

def __Target_acquired():
	__Vars = main()
	if (str(__Vars[2]) == 'None'):
		__Target = raw_input('[-] Enter Target hostname/IP: ')
		__Target_Resolved = socket.gethostbyname(__Target)
		print('[-] Target: ' + str(__Target) + ' Resolved to: ' + str(__Target_Resolved))
		return __Target
	elif(str(__Vars[2] != 'None')):
		__Target = __Vars[2]
		__Target_Resolved = socket.gethostbyname(__Target)
		print('[-] Target: ' + str(__Target) + ' Resolved to: ' + str(__Target_Resolved))
		return __Target
	return __Target

def __Port_Specified():
	__Vars = main()
	__Port_Specific = __Vars[4]
	__Target = __Vars[2]
	__Vars2 = __Load_Variables()
	__Default_Ports = __Vars2[3]

	if (__Port_Specific[0] == 0):
		__Port_Specific = __Default_Ports
		print('[-] Using default ports on target: ' + str(__Target))
		print('[-] Scanning ports: ' + str(__Port_Specific))
		return __Port_Specific
	elif (__Port_Specific[0] != 0):
		print('[-] Scanning target ' + str(__Target) + ' on port: ' + str(__Port_Specific))
		return __Port_Specific
	return __Port_Specific

def __Junk_Data():
	__Vars = main()
	print('[-] Default Junk: ' + str(__Vars[3]))
	if (str(__Vars[3]) == 'test'):
		__Junk = __Vars[3]
		print('[-] Default junk: "' + str(__Junk) + '" being sent to target.')
		return __Junk
	elif(str(__Vars[3]) != 'test'):
		__Junk = __Vars[3]
		print('[-] Using custom Junk: "' + str(__Junk) + '" to send as junk to target.')
		return __Junk

#__Logging_Enabled()
#__Target_acquired()
#__Port_Specified()

def __TimeOut():
	__SetTimeOut = input('[-] Set timeout in sec: ')
	return __SetTimeOut

def __Connect(__Target, __Port_Specific, __SetTimeOut, __Junk):
	__Logging = __Logging_Enabled()

	try:
		__Target = str(socket.gethostbyname(__Target))
		socket.setdefaulttimeout(__SetTimeOut)
		__Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		__Soc.connect((__Target, __Port_Specific[0]))
		__Soc.send(__Junk)
		__Reply = __Soc.recv(63553)
		__Soc.close()

		__Write_Recv(__Target, __Port_Specific[0], __Reply)
		if ( __Logging == 'False'):
			__Write(__Write_Recv)
	except(Exception) as E:
		__Write_Err(__Target, __Port_Specific[0], E)
		if ( __Logging == 'False'):
			__Write(__Write_Err)
		return E

def __Write(__Data):
	__Open = open("log.txt", "a")
	__Open.write(str(__Data) + '\n')
	__Open.close()

def __Write_Recv(__Target, __Port_Specific, __Reply):
	print('[-] Recieved ' + str(__Reply) + ' from ' + str(__Target) + ' on port ' +  str(__Port_Specific))

def __Write_Err(__Target, __Port_Specific, E):
	print('[-] Error: ' + str(E) + ' from ' + str(__Target) + ' on port ' + str(__Port_Specific))

def __Connect_Target():
	__Vars = main()
	__Vars2 = __Load_Variables()

	__Logging = __Logging_Enabled()
	__Target = __Target_acquired()
	__Port_Specific = __Port_Specified()
	__Junk = __Junk_Data()
	__SetTimeOut = __TimeOut()

	__Target = socket.gethostbyname(__Target)

#	print(__Logging)
#	print(__Target)
#	print(len(__Port_Specific))
#	print(__Junk)
#	print(__SetTimeOut)
	__Length = int
	__Length = len(__Port_Specific)

#	print(__Length)

	if (__Length == '1'):
		__Connect(__Target, __Port_Specific, __SetTimeOut, __Junk)
		return __Target, __Port_Specific, __SetTimeOut, __Junk, __Reply, E

	elif (__Length != '1'):
		i = 1
		while (i > __Length):
			__Connect(__Target, __Port_Specific, __SetTimeOut, __Junk)
			i = i + 1
			return __Target, __Port_Specific, __SetTimeOut, __Junk, __Reply, E

__Connect_Target()