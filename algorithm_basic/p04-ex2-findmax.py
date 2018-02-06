#!/usr/bin/python3

# find a maximum number 
# input: a list with n in length 
# output: max-number in the list

def find_max(a, i, max):
	if(i==len(a)):
		return max
	if(max<a[i]):
		max=a[i]
	return find_max(a, i+1, max)

v = [100, 17, 92, 18, 33, 58, 7, 33, 42, 99]
# print(find_max_idx(v))
print(find_max(v, 0, 0))
