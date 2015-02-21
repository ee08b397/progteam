#!/usr/bin/python

import sys
import math

if __name__ == "__main__":
	inputs = sys.stdin.readline().split()
	n = int(inputs[0])
	l = int(inputs[1])
	A = [int(x) for x in sys.stdin.readline().split()]
	A = sorted(A)
	max_gap = max(abs(A[0] - 0), abs(A[-1] - l))
	for i in range(1, len(A)):
		gap = abs(A[i] - A[i - 1]) / 2.0
		if  gap > max_gap:
			max_gap = gap
	print max_gap



	