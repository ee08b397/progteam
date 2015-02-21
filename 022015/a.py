#!/usr/bin/python

import sys
import math

if __name__ == "__main__":
	inputs = sys.stdin.readline().split()
	n = int(inputs[0])
	x = int(inputs[1])
	y = float(inputs[2]) / 100
	required = math.ceil(n * y)
	print max(0, int(required - x))
