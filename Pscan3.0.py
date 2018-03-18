import os, sys, time, socket, argparse
from threading import Thread

def __Load_Variables():
	__Logging = bool
	__Logging = False
	__LoggingPst = str
	__Target = None
	__TargetPst = str
	__Target_Resolved = None
	__Target_ResolvedPst = str
	__Default_Ports = [13,15,21,22,25,53,80,123,125,110,135,137,139,443,1433,1434,8080]
	__Default_PotsPst =str
	__Port_Specfic = None
	__Port_SpecficPst = str
	__Junk = '\x00\x00\x00\x00'
	__JunkPst = str
	__SetTimeOut = None
	return __Logging, __Target, __Target_Resolved, __Default_Ports, __Port_Specfic, __Junk, __SetTimeOut
	return __LoggingPst, __TargetPst, __Target_ResolvedPst, __Default_PortsPst, __Port_SpecficPst, __JunkPst

def main():
	###Load variables from the function __Load_Variables
	__Load_Variables()

	##Introduce the arguments parsed from the command line flags
	__Parser = argparse.ArgumentParser()
	__Parser.add_argument('-l', help='Enable logging to log.txt', action='store_false', dest='__Logging')
	__Parser.add_argument('-p', help='Supply port to be scanned', action='store', dest='__Port_Specfic', nargs='*', type=int)
	__Parser.add_argument('-j', help='Supply Junk data to be sent to the server', action='store', dest='__Junk', default='\x00\x00\x00\x00')
	__Parser.add_argument('-t', help='Supply Target in the CLI.', action='store', dest='__Target')
	Args = __Parser.parse_args()
	
	__LoggingPst = Args.__Logging
	if (str(__LoggingPst) != 'True'):

		__Load_Logging_variables(__LoggingPst)

	__JunkPst = Args.__Junk
	if (str(__JunkPst) != '\x00\x00\x00\x00'):
		__Load_Junk_Variables(__JunkPst)

	__TargetPst = Args.__Target
	if (str(__TargetPst) == 'None'):
		
		__Load_Target_Variables(__TargetPst)
		__Input_Target()
	
	__Input_TimeOut()

	__Connect_Sgl_Target(str(Args.__Port_Specfic))

	return Args
###Parse user supplied flags and place them in the correct variables.
###def __Load_Junk_Variables(Data):
###	__Load_Variables()
###	__Junk = __Parser.parse_args(Data)
###	return __Junk

def __Load_Target_Variables(__Target):
	__Load_Variables()
	print(Args.__Target)
	__Target = Args.__Target
	return __Target

def __Load_Port_Variables(__Port_Specfic):
	__Load_Variables()
	__Port_Specfic = Args.__Port_Specfic
	return __Port_Specfic

def __Load_Logging_variables(__Logging):
	__Load_Variables()
	__Logging = Args.__Logging
	return __Logging

def __Input_Target():
	__Target = raw_input('[-] Enter Target Website/IP: ')
	__Target = socket.gethostbyname(__Target)
	return __Target

def __Input_TimeOut():
	__SetTimeOut = input('[-] Enter timeout in sec: ')
	return __SetTimeOut

def __Write(__Data):
	__Open = open("Log.txt", "a")
	__Open.write(str(__Data) + '\n')
	__Open.close()

def __Connect(__Target, __Target_port, __SetTimeOut):
	try:
		socket.setdefaulttimeout(__SetTimeOut)
		__Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		__Soc.connect((__Target, __Target_port))
		__Soc.send(__Junk)
		__Reply = __Soc.recv(1024)
		__Soc.close()

		__Write_Recv()
		if ( __Logging == 'false'):
			__Write(__Write_Recv())

	except(Exception) as E:
		
		__Write_Err()

		if ( __Logging == 'false'):
			__Write(__Write_Err())

def __Write_Recv(__Target, __Port_Specfic, __SetTimeOut, __Reply):
	print('[-] Recieved ' + str(__Reply) + ' from host: ' + __Target + ' on port: ' + __Port_Specfic)
	
def __Write_Err(__Target, __Port_Specfic, __SetTimeOut, E):
	print('[-] Error ' + str(__Target) + str(E) + ' on port: ' + str(__Port_Specfic))	 
	
def __Connect_Sgl_Target(__Port_Specfic):
	i = 0
	if ( len(__Port_Specfic[i]) == 0):
		print(str(__Port_Specfic))
		T = Thread(__Connect(__Target, __Port_Specfic[i], __SetTimeOut))
		T.start()
		i = i + 1

if __name__ == '__main__':
	main()