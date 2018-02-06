#!/usr/bin/python3

# Sequential search (3)
# input: 
#		a: list of student's no
# 		b: list of student's name corresponding to list 'a'
#		x: student's number to search
# output: student's name on success, otherwise '?'.

def search_name(a, b, x):

	na=len(a)
	nb=len(b)
	if na!=nb :
		return "incorrect list pair"

	for i in range(0, na):
		if x == a[i]:
			return b[i]

	return "?"

# main

stu_no = [39, 14, 67, 105]
stu_name = ["Justin", "John", "Mike", "Summer"]

print(search_name(stu_no, stu_name, 39))
print(search_name(stu_no, stu_name, 15))
print(search_name(stu_no, stu_name, 105))

