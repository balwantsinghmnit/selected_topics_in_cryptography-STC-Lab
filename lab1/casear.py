import string

letters = string.ascii_lowercase
cap = string.ascii_uppercase


file1 = open("input.txt","r")
file2 = open("key.txt","r")

p = file1.readline()
f2 = file2.readline()

k = f2[0]
c  = ""

for i in range(len(p)):
	if p[i]==" ":
		continue
	temp = p[i]
	if temp in cap:
		c += cap[(ord(temp)-65+ord(k)-65)%26]
	else:
		c += letters[(ord(temp)-97+ord(k)-97)%26]

p = ""

for i in range(len(c)):
	flag = 0
	if c[i] in cap:
		flag=1
	temp = ord(c[i])-ord(k)
	if temp<0:
		temp += 26
	temp %= 26
	if flag==1:
		p += cap[temp]
	else:
		p += letters[temp]

out = open("output.txt","w")
out.write(c)