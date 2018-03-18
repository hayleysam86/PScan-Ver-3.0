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
	
	return Args

def print_Vars(__Logging, __LoggingPst, __Target, __TargetPst):
	print(str(__Logging))
	print(str(__LoggingPst))
	print(str(__Target))
	print(str(__TargetPst))
#	print(str(__Target_Resolved))
#	print(str(__Target_ResolvedPst))
#	print(str(__Default_Ports))
#	print(str(__Default_PortsPst))
#	print(str(__Port_Specfic))
#	print(str(__Port_SpecficPst))
#	print(str(__Junk))
#	print(str(__JunkPst))

if __name__ == '__main__':
	main()
	__Parser = argparse.ArgumentParser()
	Args = __Parser.parse_args()
	print_Vars(__Logging, __LoggingPst, __Target, __TargetPst)