#!/bin/python3

import turtle as t 

# x-coordinate range to draw a graph
x_min = -5
x_max = +5

# y-coordinate range to draw a graph
y_min = -5
y_max = +5

# interval at which to draw the graph
space = 0.01

# drawing function list
func_list = ["y=x*x", "y=abs(x)", "y=0.5*x+1"]

#setting up coordinates, turtle speed, and line width
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

# draw x-axis
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

# draw y-axis
t.up()
t.goto(y_min, 0)
t.down()
t.goto(y_max, 0)

# draw graphs
t.color("green")

for func in func_list:
	x = x_min
	exec(func)
	t.up()
	t.goto(x, y)
	t.down()
	while x <= x_max:
		x=x+space
		exec(func)
		t.goto(x, y)

t.mainloop()


# appendix. refer https://www.wolframalpha.com/
