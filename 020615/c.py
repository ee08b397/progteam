import sys

class Node(object):
	def __init__(self, index, data):
		self.data = data
		self.index = index

parts = sys.stdin.readline().split()
n = int(parts[0])
k = int(parts[1])
arr = [Node(i, int(x)) for i, x in enumerate(sys.stdin.readline().split())]
sorted_arr = sorted(arr, key=lambda node: node.data)
count = 0
days = 0
solution = []
for e in sorted_arr:
	days += e.data
	if days > k:
		break
	count += 1
	solution.append(e.index + 1)
print count
if count > 0:
	print " ".join([str(x) for x in solution])
	
