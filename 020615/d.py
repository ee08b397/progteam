import sys

if __name__ == "__main__":
	s = sys.stdin.readline().strip()
	left = 0
	right = len(s) - 1
	insert = 0 
	while left <= right and insert < 3:
		if s[left] != s[right]:		
			if insert == 0:
				temp = s
				s = temp[0:left] + temp[right] + temp[left:]	
				right += 1
				print s
			elif insert == 1:
				s = temp[0:(right + 1)] + temp[left] + temp[(right + 1):]
				left -= 1
				print s
			insert += 1
			print "%r %r" % (left, right)
		else:
			left += 1
			right -= 1

	if insert == 3:
		print "NA"
	elif insert == 0:
		s = s[left - 1] + "a" + s[left:]	
	else:
		print s
