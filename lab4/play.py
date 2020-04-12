s = "abcdefghijklmnopqrstuvwxyz"
letters = list(s)

def findrc(c,k):
	for i in range(5):
		for j in range(5):
			if k[i][j]==c:
				return([i,j])

def encrypt(pair,k):
	first = findrc(pair[0],k)
	second = findrc(pair[1],k)
	s = ""
	if first[0]==second[0]:
		s = k[first[0]][(first[1]+1)%5]+k[first[0]][(second[1]+1)%5]
		return(s)
	elif first[1]==second[1]:
		s = k[(first[0]+1)%5][first[1]]+k[(second[0]+1)%5][second[1]]
		return(s)
	else:
		s = k[first[0]][second[1]]+k[second[0]][first[1]]
		return(s)

def decrypt(pair,k):
	first = findrc(pair[0],k)
	second = findrc(pair[1],k)
	s = ""
	if first[0]==second[0]:
		first[1] -= 1
		second[1] -= 1
		if first[1]<0:
			first[1] += 5
		if second[1]<0:
			second[1] += 5
		s = k[first[0]][first[1]]+k[first[0]][second[1]]
		return(s)
	elif first[1]==second[1]:
		first[0] -= 1
		second[0] -= 1
		if first[0]<0:
			first[0] += 5
		if second[0]<0:
			second[0] += 5
		s = k[first[0]][first[1]]+k[second[0]][second[1]]
		return(s)
	else:
		s = k[first[0]][second[1]]+k[second[0]][first[1]]
		return(s)


d = dict()
for i in range(len(letters)):
	d[letters[i]] = 0

inp = open('input.txt','r')
p = inp.readline()

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
			while d[letters[count]]==1:
				count += 1
			if letters[count]=='j':
				count += 1
			d[letters[count]]=1
			k[i][j] = letters[count]
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


