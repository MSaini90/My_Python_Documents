# parse.arge = Function is used for parsed all arguments
# add_arguments = Function is used for add add_arguments
# ArgumentParser() = It is a class which i make object
# stdout = Give standard output of console

import argparse
import sys


def calc(args):
	if args.o == 'add':
		return args.x + args.y

	elif args.o == 'mul':
		return args.x * args.y

	elif args.o == 'sub':
		return args.x - args.y

	elif args.o == 'div':
		return args.x / args.y
	
	else:
		return "Something went wrong"


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--x' , type = float , default = 1.0 ,
	help = "Enter the first number. This is a utility for calculations. Please contact with Mohit bhai")

	parser = argparse.ArgumentParser()
	parser.add_argument('--y' , type = float , default = 3.0 ,
	help = "Enter the second number. This is a utility for calculations. Please contact with Mohit bhai")

	parser = argparse.ArgumentParser()
	parser.add_argument('--o' , type = str , default = "add" ,
	help = "This is a utility for calculations. Please contact with Mohit bhai for more")
	
	args = parser.parse_args()
	sys.stdout.write(str(calc(args)))