#!/usr/bin/python

import sys

def solveMirror(grid, N):
	for i in reversed(range(N)):
		for j in reversed(range(N)):
			


T = int(sys.stdin.readline())
for t in range(T):
	N = int(sys.stdin.readline()) 
	grid = []
	for n in range(N):
		grid.append(sys.stdin.readline())
	print solveMirror(grid, N)