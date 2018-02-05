# Program to calculate Mean, Variance, and Standard deviation.

import math

# data list
d = [1,2,3,4,5]
print(d)

# calculate mean
mean = sum(d)/len(d)
print(mean)

# calculate variance
vsum = 0
for x in d:
	vsum = vsum + (x-mean)**2
var = vsum/len(d)
print(var)

# calculate SD(standard deviation)
std = math.sqrt(var)
print(std)

