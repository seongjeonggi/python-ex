#!/usr/bin/python3

# find a position of the maximum number 
# input: a list of n-length 
# output: position of max-number among numbers in length n. 
#         (value is the range in 0~n-1)

def find_max_idx(a):
	n = len(a)
	max_idx = 0
	for i in range(1, n):
		if a[i] > a[max_idx]:
			max_idx = i
	return max_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
# print(find_max_idx(v))
print(v[find_max_idx(v)])
