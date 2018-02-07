#!/usr/bin/python3

# Check palindrome (using the feature of Queue and Stack)
# input: string s
# output: True if s is palindrome, otherwise False

def palindrome(s):

	# Declare Queue and Stack, as a list type.
	qu = []
	st = []

	# Step 1: Insert a character of a string "s" into Queue and Stack respectively.
	for x in s:
		# If this character is the alphabet(if not space, numeric, special), 
		# Add the character into Queue and Stack respectively.
		if x.isalpha():
			qu.append(x.lower())
			st.append(x.lower())
	# Step 2: Compare each character from the Queue and Stack.
	while qu: # Repeat until the Queue is empty.
		if qu.pop(0) != st.pop(): # Not the palindrome if two characters are different.
			return False

	return True

# start main

print(palindrome("Wow"))
print(palindrome("Madam, I'm Adam."))
print(palindrome("Madam, I am Adam."))

# use collections module

from collections import deque
qu = deque()
qu.append(1)	# enqueue 1
qu.append(2)	# enqueue 2
print(qu)

qu.popleft()	# dequeue => 1
print(qu)
