#!/usr/bin/python3

# find a maximum number 
# input: a list with n in length 
# output: max-number in the list

def find_max(a, n):
	if n == 1:
		return a[0]
	max_n_1 = find_max(a, n-1)
	
	if max_n_1 > a[n-1]:
		return max_n_1
	else:
		return a[n-1]

v = [100, 17, 92, 18, 33, 58, 7, 33, 42, 99]
print(v)
print(find_max(v, len(v)))
