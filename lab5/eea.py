def gcd(a,b):
	if a>b:
		a,b=b,a
	if b%a==0:
		return(a)
	else:
		return(gcd(a,b%a))

def verify(n,m,x):
	print("verification::")
	print(n,"*",x,"mod(",m,") =",(n*x)%m)

inp = open("input.txt","r")
n = int(inp.readline())
m = int(inp.readline())

if(gcd(n,m)!=1):
	print("Inverse not possible!!")
else:
	i=1
	while (n*i)%m!=1:
		i += 1
	out = open("output.txt","w")
	out.write(str(i))
	out.close()
	print("inverse :",i)
	verify(n,m,i)
