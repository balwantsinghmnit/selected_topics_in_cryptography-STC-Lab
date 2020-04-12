import string

letters = string.ascii_lowercase
upper = string.ascii_uppercase
letters = letters + upper

inp = open("input.txt","r")
p = inp.readline()
inp.close()

key = open("key.txt","r")
k1 = key.readline()
key.close()
k = ""

for i in range(len(p)):
	if i%len(k1)==0:
		count = 0
	k += k1[count]
	count += 1

c = ""

for i in range(len(p)):
	if p[i]==" ":
		c += "#"
	else:
		index1 = letters.index(p[i])
		index2 = letters.index(k[i])
		index = (index1+index2)%52
		c += letters[index]

out = open("output.txt","w")
out.write(c)
out.close()
print("Encryption Done!!!")
print("enter 1 to decrypt")
choice = int(input())
#*********************************************************************************************************
def convert(x,y):
	index = x- y
	if index<0:
		index += 52
	return(index)

if choice==1:
	out = open("output.txt","r")
	c = out.readline()

	p = ""
	for i in range(len(c)):
		if c[i]=="#":
			p += " "
		else:
			index1 = letters.index(c[i])
			index2 = letters.index(k[i])
			index = convert(index1,index2)
			p += letters[index]

	out = open("input.txt","w")
	out.write(p)
	out.close()
	print("Decryption Done!!")


