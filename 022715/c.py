#!/usr/bin/python2

# Vitaly is a diligent student who never missed a lesson in his five years of studying in the university. He always does his homework on time and passes his exams in time.
# During the last lesson the teacher has provided two strings s and t to Vitaly. The strings have the same length, they consist of lowercase English letters, string s is lexicographically smaller than string t. Vitaly wondered if there is such string that is lexicographically larger than string s and at the same is lexicographically smaller than string t. This string should also consist of lowercase English letters and have the length equal to the lengths of strings s and t. 

import sys

s = list(sys.stdin.readline().strip())
t = sys.stdin.readline().strip()

z = len(s) - 1
s[z] = chr(ord(s[z]) + 1)
while z > 0 and ord(s[z]) > ord('z'):
	s[z] = 'a'
	z -= 1
	s[z] = chr(ord(s[z]) + 1)

s = "".join(s)
if s < t:
	print s
else:
	print "No such string"