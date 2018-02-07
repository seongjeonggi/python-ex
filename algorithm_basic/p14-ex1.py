#!/usr/bin/python3

# Dictionary search
# input: 
#		a: dictionary of student's no.(key) and name(value)
#		x: student's number to search
# output: student's name on success, otherwise '?'.

def search_name(a, x):

	keys = a.keys()
	for k in keys:
		if k == x:
			return a[x]
	
	return "?"

# main

stu_nn = {39:"Justin", 14:"John", 67:"Mike", 105:"Summer"}

print(search_name(stu_nn, 39))
print(search_name(stu_nn, 15))
print(search_name(stu_nn, 105))
print(search_name(stu_nn, 14))
