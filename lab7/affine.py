#Python3 code for affine cipher
#Encryption:-  E(x) = (a*x+b)mod26
#Decryption:-  D(x) = (multiplicative_inverse_of_a*(x-b))mod26

#function for calculating multiplicative inverse
def modInverse(a, m=26) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

#function to encrypt the input text letters
def encrypt(a,b,m):
	x = ord(m)-97
	return chr((a*x+b)%26+97)

#function to decrypt the input text letters
def decrypt(a,b,m):
	a = modInverse(a)
	x = ord(m)-97
	return chr((a*(x-b))%26+97)


#let's load input file and read the input
input_file = open("input.txt","r")
inp = input_file.readline()
inp=inp.lower()

#let's load key file and read values of our two keys a & b
key_file = open("key.txt","r")
a = int(key_file.readline())
b = int(key_file.readline())

#initialise empty ciphertext
cipher = ""

#using loops let's encrypt the input text letters one by one
for i in range(len(inp)):
	cipher += str(encrypt(a,b,inp[i]))

#create new file output.txt and write the ciphertext in that
output = open("output.txt","w")
output.write(cipher)
output.close()

#print a message on the terminal
print("Encryption done!!! check output.txt file & Enter 1 for decryption anything else for stop the program")

#take user's choice
choice = input()

#check the choice
if(choice=='1'):
	#load & read the content of output.txt file
	out = open("output.txt","r")
	cipher = out.readline()
	out.close()

	#initialise empty plaintext
	plaintext = ""

	#using loops let's decrypt the input text letters one by one
	for i in range(len(cipher)):
		plaintext += str(decrypt(a,b,cipher[i]))

	#create new file input2.txt and write the plaintext in that
	input2 = open("input2.txt","w")
	input2.write(plaintext)
	input2.close()

	#print a message on the terminal
	print("Decryption done!!! check input2.txt file")