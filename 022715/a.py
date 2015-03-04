#!/usr/bin/python2

import sys

a, b, s = [abs(int(x)) for x in sys.stdin.readline().split()]

if s < a + b:
	print "No"
elif s == a + b:
	print "Yes"
else:
	if (a + b) % 2 == 0 and s % 2 == 0: 
		print "Yes"
	elif (a + b) % 2 == 1 and s % 2 == 1:
		print "Yes"
	else:
		print "No"