import socket;
import pprint;
import array;
import pip._vendor.ipaddress;

TargetPort = ''
TargetAddr = ''
commonPorts = ''

def __main__():
	TargetAddr = raw_input('Enter Target IP address: ')
	ip_Target = pip._vendor.ipaddress.ip_address(unicode(TargetAddr))
	TargetPort = raw_input('Enter Target port: ')

	__PortArray__()
	__SocketConnect__(ip_Target, TargetPort)

	print(str(replyStr))

	if TargetPort is 'All':
		while __SocketConnect__:
			TargetPort = int(commonPorts[i])
			int(i)+1

		return TargetPort, TargetAddr, ip_Target

def __PortArray__():
	commonPorts = array.array('i',(13,21,22,80,8080))



def __SocketConnect__(TargetPort, ip_Target):
	socket.setdefaulttimeout(2)
	s = socket.socket()
	s.connect((ip_Target, TargetPort))
	reply = s.recv(1024)
 	return reply

def __newprint__(reply):
	replyStr = str(reply)
	return replyStr

if __name__ == "__main__":
	__main__()
