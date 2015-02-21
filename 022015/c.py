#!/usr/bin/python

import sys

if __name__ == "__main__":
	inputs = sys.stdin.readline().split()
	N = int(inputs[0])
	M = int(inputs[1])
	A = [int(x) for x in sys.stdin.readline().split()]

	total = 0
	for i in range(M):
		inputs = sys.stdin.readline().split()
		if inputs[0] == "R":
			print A[(total + int(inputs[1])) % N - 1]
		elif inputs[0] == "C":
			total += int(inputs[1])
		elif inputs[0] == "A":
			total -= int(inputs[1])

