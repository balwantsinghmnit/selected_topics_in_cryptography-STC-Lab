import string

letters = string.ascii_lowercase
cap = string.ascii_uppercase


file1 = open("input.txt","r")
file2 = open("key2.txt","r")

p = file1.readline()

k1 = []
k2 = []
for i in range(26):
	s = file2.readline()
	k1.insert(i,s[0])
for i in range(26):
	s = file2.readline()
	k2.insert(i,s[0])

c  = ""

for i in range(len(p)):
	if p[i]==" ":
		continue
	temp = p[i]
	if temp in cap:
		kindex = cap.index(temp)
		c += k2[kindex]
	else:
		kindex = letters.index(temp)
		c += k1[kindex]

p = ""

for i in range(len(c)):
	if c[i] in cap:
		lindex = k2.index(c[i])
		p += cap[lindex]
	else:
		lindex = k1.index(c[i])
		p += letters[lindex]


inp = open("input2.txt","w")
out = open("output.txt","w")
inp.write(p)
out.write(c)