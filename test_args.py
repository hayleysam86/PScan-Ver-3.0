def __Test():
	Variable_one = 'test'
	Variable_Two = 'Test'
	return Variable_one, Variable_Two

def main():
	variables = __Test()
	print(str(variables[0]))
	print(str(variables[1]))

main()