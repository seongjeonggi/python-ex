#!/usr/bin/python3

# Hanoi tower
# input: 
#		n = the number of a disk to move
#		from_pos = starting pole which has a disk to move.
# 		to_pos = destination pole to move a disk.
#		aux_pos = auxiliary pole to move a disk
# output: the order of moving disk.

def hanoi(n, from_pos, to_pos, aux_pos):
	if n==1:
		print(from_pos, "->", to_pos)
		return

	hanoi(n-1, from_pos, aux_pos, to_pos)
	print(from_pos, "->", to_pos)

	hanoi(n-1, aux_pos, to_pos, from_pos)
	
# main

print("n = 1")
hanoi(1, 1, 3, 2)

print("n = 2")
hanoi(2, 1, 3, 2)

print("n = 3")
hanoi(3, 1, 3, 2)

print("n = 5")
hanoi(5, 1, 3, 2)