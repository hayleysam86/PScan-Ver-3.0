import argparse
import math
import os
import sys

port = 0

__Parse = argparse.ArgumentParser()
__Parse.add_argument('-p', action='store', nargs='*', dest='port')
args = __Parse.parse_args()

print(str(args.port))

count_ports = len(args.port)

print(str(count_ports))