from matplotlib import pyplot as plt
import string
import numpy as np

lower = string.ascii_lowercase
upper = string.ascii_uppercase

inp = open("input.txt","r")
out = open("output.txt","r")

p = inp.readline()
c = out.readline()

x = [i for i in range(1,27)]
y = [0]*26

for i in range(len(p)):
	if p[i]==" ":
		continue
	else:
		if p[i] in lower:
			index = lower.index(p[i])
		else:
			index = upper.index(p[i])
		y[index] += 1

plt.hist(y,bins=26)

y = [0]*26

for i in range(len(c)):
	if c[i]=="#":
		continue
	else:
		if c[i] in lower:
			index = lower.index(c[i])
		else:
			index = upper.index(c[i])
		y[index] += 1
plt.hist(y,bins=26)

plt.show()