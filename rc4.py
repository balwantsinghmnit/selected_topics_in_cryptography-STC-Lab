#rc4 python3 code

#pow function
def pow(a,b):
	ans=1
	for i in range(b):
		ans *= a
	return ans

#encryption function
def encrypt(p,k,n):
	n = pow(2,n)
	#key schedule algorithm
	j=0
	S = []
	for i in range(n):
		S.append(i)
	T= []
	for i in range(n):
		T.append(k[i%len(k)])
	#scrambling
	for i in range(n):
		j = (j + S[i]+T[i])%n
		S[i],S[j] = S[j],S[i]


	#rec4 keystream generation
	i,j=0,0
	c = []
	for m in range(len(p)):
		i = (i+1)%n
		j = (j+S[i])%n
		S[i],S[j]=S[j],S[i]
		k[m] = S[(S[i]+S[j])%n]
		c.append(p[m]^k[m])

	ks,cs = "",""
	for i in range(len(p)):
		ks += str(k[i])+" "
		cs += str(c[i])+" "

	#let's write result in output file
	out = open("output.txt","w")
	out.write("k : "+ks+"\n"+"c : "+cs)
	out.close()
	print("encryption done!! check output.txt")

n = int(input("Enter word size of the algorithm"))

#read input and key value
inp_file = open("input.txt","r")
p = list(map(int,inp_file.readline().split()))

key_file = open("key.txt","r")
k = list(map(int,key_file.readline().split()))

encrypt(p,k,n)