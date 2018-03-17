import argparse

def main():
	logging_enabled = bool
	port = 0
	__Parser = argparse.ArgumentParser()
	__Parser.add_argument('-l', action='store_false', dest='logging_enabled')
	__Parser.add_argument('-p', action='store', nargs='*', dest='port')
	
	args = __Parser.parse_args()

	print(args.port)

	if(args.port != 0):
		print(str(args.port))

	print(str(args.logging_enabled))
	if (str(args.logging_enabled) == 'False'):
		print("Logging is enabled! Writing to log.txt!")
	if (str(args.logging_enabled) == 'True'):
		print("Logging is not enabled!")

if __name__ == '__main__':
	main()