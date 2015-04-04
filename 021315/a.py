#!/usr/local/python

# Today Chef wants to clean his garden. Chef has N columns of ground. Each column has it's height . Chef can choose any column and increase its height by 1 using 1 cube of ground.
# Chef wants to spend exactly M cubes. Can he make this in such way that the heights of all columns will become equal?
# Input
#     First line of input contains an integer T denoting number of test cases.
#     Then for each test case, The first line contains two integers N and M.
#     The second line contains N space-separated integers A1, A2, ..., AN denoting the initial heights of the columns".
# Output
#     If Chef can spend all cubes and make the columns equal print Yes else print No.


import sys

if __name__ == "__main__":

	T = int(sys.stdin.readline())
	for t in range(T):
		inputs = sys.stdin.readline().split()
		N = int(inputs[0])
		M = int(inputs[1])
		inputs = sys.stdin.readline()
		A = [int(x) for x in inputs.split()]
		tallest = max(A)	
		for a in A:
			M -= (tallest - a)
		if M >= 0 and M % N == 0:
			print "Yes"
		else:
			print "No"