#!/usr/local/python

import sys

if __name__ == "__main__":
	inputs = sys.stdin.readline().split()
	N = int(inputs[0])
	M = int(inputs[1])
	across = "#" * M
	right = "." * (M - 1) + "#"
	left = "#" + "." * (M - 1)
	flip = 0
	for n in range(1, N + 1):
		if n % 2 != 0:
			print across
		else:
			if flip == 0:
				flip = 1
				print right
			else:
				flip = 0
				print left

