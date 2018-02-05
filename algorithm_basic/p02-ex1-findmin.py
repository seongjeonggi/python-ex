#!/usr/bin/python3

# find a position of the minimum number 
# input: a list of n-length 
# output: position of min-number among numbers in length n. 
#         (value is the range in 0~n-1)

def find_min(a):
	n = len(a)
	min_idx = 0
	for i in range(1, n):
		if a[i] < a[min_idx]:
			min_idx = i
	return a[min_idx]

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))
