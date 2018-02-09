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

	if left == right:
		return left

	half = (right-left+1)//2
	g1_left = left
	g1_right = left+half-1
	g2_left = left+half
	g2_right = g2_left+half-1

	result = weight(g1_left, g1_right, g2_left, g2_right)

	if result == -1:
		return find_fakecoin(g1_left, g1_right)
	elif result == 1:
		return find_fakecoin(g2_left, g2_right)
	else:
		return right


# start main
fake = 29
n = 100
print(find_fakecoin(0, n-1))

