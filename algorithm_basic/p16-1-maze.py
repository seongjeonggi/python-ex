#!/usr/bin/python3

# Maze search - Graph
# input: g: maze info, start: start point, end: end point
# output: string of maze path, or print "?" if no solution.

def solve_maze(g, start, end):
	qu = []
	done = set()

	qu.append(start)
	done.add(start)

	while qu:
		p = qu.pop(0)
		v = p[-1]
		if v == end:
			return p
		
		for x in g[v]:
			if x not in done:
				qu.append(p+x)
				done.add(x)

	return "?"

# maze info.

maze = {
	'a': ['e'],
	'b': ['c', 'f'],
	'c': ['b', 'd'],
	'd': ['c'],
	'e': ['a', 'i'],
	'f': ['b', 'g', 'j'],
	'g': ['f', 'h'],
	'h': ['g', 'l'],
	'i': ['e', 'm'],
	'j': ['f', 'k', 'n'],
	'k': ['j', 'o'],
	'l': ['h', 'p'],
	'm': ['i', 'n'],
	'n': ['m', 'j'],
	'o': ['k'],
	'p': ['l']
}

print(solve_maze(maze, 'a', 'p'))
