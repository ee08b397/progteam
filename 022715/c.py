#!/usr/bin/python2

import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

output = ""
found = False
for i in range(len(s)):
	if ord(t[i]) - ord(s[i]) > 1 or (ord(t[i]) > ord(s[i]) and i != len(s) - 1):
		found = True
		output += chr(ord(t[i])-1)
		output += t[i+1:]
		break
	else:
		output += t[i]

if found:
	print output
else:
	print "No such string"