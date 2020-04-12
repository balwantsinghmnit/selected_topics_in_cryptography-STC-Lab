import string

lower = string.ascii_lowercase


def encrypt(pair,k):
	r1=r2=c1=c2=-1
	for i in range(5):
		for j in range(5):
			if k[i][j]==pair[0]:
				r1,c1 = i,j
				break
		if r1>=0:
			break
	for i in range(5):
		for j in range(5):
			if k[i][j]==pair[1]:
				r2,c2 = i,j
				break
		if r2>=0:
			break
	s = ""
	if r1==r2:
		s = k[r1][(c1+1)%5]+k[r1][(c2+1)%5]
		return(s)
	elif c1==c2:
		s = k[(r1+1)%5][c1]+k[(r2+1)%5][c2]
		return(s)
	else:
		s = k[r1][c2]+k[r2][c1]
		return(s)
def decrypt(pair,k):
	r1=r2=c1=c2=-1
	for i in range(5):
		for j in range(5):
			if k[i][j]==pair[0]:
				r1,c1 = i,j
				break
		if r1>=0:
			break
	for i in range(5):
		for j in range(5):
			if k[i][j]==pair[1]:
				r2,c2 = i,j
				break
		if r2>=0:
			break
	s = ""
	if r1==r2:
		c1 -= 1
		c2 -= 1
		if c1<0:
			c1 += 5
		if c2<0:
			c2 += 5
		s = k[r1][c1]+k[r1][c2]
		return(s)
	elif c1==c2:
		r1 -= 1
		r2 -= 1
		if r1<0:
			r1 += 5
		if r2<0:
			r2 += 5
		s = k[r1][c1]+k[r2][c2]
		return(s)
	else:
		s = k[r1][c2]+k[r2][c1]
		return(s)


d = dict()
for i in range(len(lower)):
	d[lower[i]] = 0

inp = open('input.txt','r')
pt = inp.readlines()
p=""
for i in range(len(pt)):
	p += pt[i]

key = open('key.txt','r')
word = key.readline()

k = [0]*5
for i in range(5):
	k[i] = [0]*5
count=0
flag=0
for i in range(5):
	for j in range(5):
		if flag==0:
			while d[word[count]]==1:
				count += 1
			if word[count]=='j':
				count += 1
			d[word[count]]=1
			k[i][j] = word[count]
			count += 1
			if count==len(word):
				flag=1
				count=0
		else:
			while d[lower[count]]==1:
				count += 1
			if lower[count]=='j':
				count += 1
			d[lower[count]]=1
			k[i][j] = lower[count]
			count += 1
for i in range(5):
	print(k[i])

if len(p)%2==1:
	p += "z"

c = ""
for i in range(0,len(p),2):
	pair = p[i:i+2]
	c += encrypt(pair,k)

out = open('output.txt','w')
out.write(c)
out.close()
inp.close()
print('incryption done!!!')	

n = int(input("Enter 1 for decryption"))
if n==1:
	out = open('output.txt','r')
	c = out.readline()
	p = ""
	for i in range(0,len(c),2):
		pair = c[i:i+2]
		p += decrypt(pair,k)
	inp = open('input.txt','w')
	inp.write(p)
	print('decryption done!!!')	


