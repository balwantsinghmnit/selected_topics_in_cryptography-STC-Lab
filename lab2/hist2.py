from matplotlib import pyplot as plt
import string
import numpy as np

lower = string.ascii_lowercase
upper = string.ascii_uppercase

inp = open("inputt.txt","r")
out = open("outputt.txt","r")

p = inp.readline()
p = inp.readline()
c = out.readline()

x = [i for i in range(1,27)]
y = [0]*26

for i in range(len(p)):
	if p[i]==" ":
		continue
	else:
		if p[i] in upper:
			index = upper.index(p[i])
		else:
			index = lower.index(p[i])
		y[index] += 1

plt.plot(x,y)

y = [0]*26

for i in range(len(c)):
	if c[i]==" ":
		continue
	else:
		if c[i] in lower:
			index = lower.index(c[i])
		else:
			index = upper.index(c[i])
		y[index] += 1
plt.plot(x,y)

plt.show()
