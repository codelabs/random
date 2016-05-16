import sys

def main(args):
	print "Filename : " + args[0]
	for i in range(1, len(args)):
		sys.stdout.write("Argument %2i : %s\n" % (i, args[i]))

# By default, if this file is not part of a package,
# python assumes package name as __main__
# Checking if current package is __main__ or not
# and if it is, check the command line args
if __name__ == '__main__':

	# If no args are passed, print error and exit
	if len(sys.argv) == 1:
		sys.stderr.write("Cannot have zero command line args\n")
		sys.exit(1)

	# Call the main function
	# after validating args
	main(sys.argv)
