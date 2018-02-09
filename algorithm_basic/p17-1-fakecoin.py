#!/usr/bin/python3

# Search Fake coin
# input: range of whole coin. 0~n-1
# output: index of fake coin

global fake

def weight(a, b, c, d):
	
	if a <= fake and fake <= b:
		return -1
	if c <= fake and fake <= d:
		return 1

	return 0

def find_fakecoin(left, right):
	for i in range(left+1, right+1):
		result = weight(left, left, i, i)
		if result == -1:
			return left
		elif result == 1:
			return i

	return -1

# start main
fake = 29
n = 100
print(find_fakecoin(0, n-1))

