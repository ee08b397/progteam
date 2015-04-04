# According to the regulations of Berland's army, a reconnaissance unit should consist of exactly two soldiers. Since these two soldiers shouldn't differ much, their heights can differ by at most d centimeters. Captain Bob has n soldiers in his detachment. Their heights are a1, a2, ..., an centimeters. Some soldiers are of the same height. Bob wants to know, how many ways exist to form a reconnaissance unit of two soldiers from his detachment.
# Ways (1, 2) and (2, 1) should be regarded as different.

#!/usr/local/bin/python
import sys

line = sys.stdin.readline().split()
n, d = int(line[0]), int(line[1])
A = [int(x) for x in sys.stdin.readline().split()]
count = 0
for i in range(n):
	for j in range(i + 1, n)
		if abs(A[i] - A[j]) < d:
			count += 2

print count
