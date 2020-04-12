import numpy
#input a three letter input in input.txt 
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
def getCofactor(A,temp,p,q,n):
	temp1 = [[0]*3 for i in range(3)]
	for i in range(3):
		for j in range(3):
			temp1[i][j]=temp[i][j]
	i = j = 0
	for row in range(n):
		for col in range(n):
			if row != p and col != q:
				temp1[i][j] = A[row][col]
				j += 1
				if j == n - 1:
					j = 0
					i += 1
	return temp1

def determinant(A,n):
	D = 0
	if (n == 1):
		return A[0][0]
	temp = [[0]*len(A) for i in range(len(A))]
	sign = 1

	for f in range(n):
		temp=getCofactor(A, temp, 0, f, n)
		D += sign * A[0][f] * determinant(temp, n - 1)
		sign = -sign
	return D

def adjoint(A,temp1):
	if len(A)==1:
		adj[0][0]=1
		return adj
	sign = 1
	n=len(A)
	adj = [[0]*3 for i in range(3)]
	for i in range(3):
		for j in range(3):
			adj[i][j]=temp1[i][j]
	temp = [[0]*3 for i in range(3)]

	for i in range(n):
		for j in range(n):
			temp=getCofactor(A, temp, i, j, n)
			if (i+j)%2==0:
				sign=1
			else:
				sign=-1
			adj[j][i] = (sign)*(determinant(temp, n-1))
	return(adj)
def find_inverse(Mat):
	d=determinant(Mat,len(Mat))
	b=adjoint(Mat,Mat)
	minv = modInverse(d,26)
	for i in range(3):
		for j in range(3):
			b[i][j] *= minv
			b[i][j] %= 26
	return b

def encrypt(inp_vector,c_Mat,Mat): 
	for i in range(3): 
		for j in range(1): 
			c_Mat[i][j] = 0
			for x in range(3): 
				c_Mat[i][j] += (Mat[i][x] *
									inp_vector[x][j]) 
			c_Mat[i][j] = c_Mat[i][j] % 26
	return c_Mat
def decrypt(c_Mat,inp_mat,inverse): 
	for i in range(3): 
		for j in range(1): 
			inp_mat[i][j] = 0
			for x in range(3): 
				inp_mat[i][j] += (inverse[i][x] *
									c_Mat[x][j]) 
			inp_mat[i][j] = inp_mat[i][j] % 26
	return inp_mat

inpfile = open("input.txt","r")
inp = inpfile.readline()
keyfile = open("key.txt","r")
key = keyfile.readline()
matrix = open("kmatrix.txt","a")

k = 0
Mat = [[0] * 3 for i in range(3)]
for i in range(3):
	for j in range(3):
		Mat[i][j] = ord(key[k]) % 97
		matrix.write(str(Mat[i][j])+"\n")
		k += 1
matrix.close()

inp_vector = [[0] for i in range(3)]
for i in range(3):
	inp_vector[i][0] = ord(inp[i]) % 97

c_Mat = [[0] for i in range(3)]
c_Mat = encrypt(inp_vector,c_Mat,Mat)

cipher = []

for i in range(3):
	cipher.append(chr(c_Mat[i][0] + 97))

out = open("output.txt","w")
out.write("".join(cipher))
out.close()
print("encryption done!! check the output file")

print("Enter 1 for decryption ,anything else for not")
choice = input()
if choice=="1":
	inverse = find_inverse(Mat)
	inp_mat = [[0] for i in range(3)]
	inp_mat = decrypt(c_Mat,inp_mat,inverse)
	inp = []

	for i in range(3):
		inp.append(chr(int(inp_mat[i][0]) + 97))

	out = open("input2.txt","w")
	out.write("".join(inp))
	print("decryption done!! check the input2 file")
	out.close()
inpfile.close()
keyfile.close()



