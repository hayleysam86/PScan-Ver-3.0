from optparse import OptionParser

Logging_enabled = bool
Logging_enabled = False

def main():
	__Parser = OptionParser()
	__Parser.add_option('-l', '--log', action='store_true', dest='Logging_enabled')
	options, args = __Parser.parse_args()
	print(str(options))

if __name__ == "__main__":
	main()	