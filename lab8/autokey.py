#Auto key cipher implemented in python3
#this cipher is like vigener cipher but more secure than that

#import string for using alphabets
import string

#store all the english letters
letters = string.ascii_lowercase

#function for encrption
def encryption(inp,key):
	global letters
	#create new empty ciphertext variable
	cipher = ""
	#encrypt all the letters one by one now
	for i in range(len(inp)):
		#find index of both letters in plaintext & key in letters, let say a & b
		a = letters.index(inp[i])
		b = letters.index(key[i])
		#find new encrypted letter
		cipher += letters[(a+b)%26]
	return(cipher)

#function for decrption
def decryption(cipher,key):
	global letters
	#create new empty plaintext variable
	plaintext = ""
	#decrypt all the letters one by one now
	for i in range(len(cipher)):
		#find index of both letters in ciphertext & key in letters, let say a & b
		a = letters.index(cipher[i])
		b = letters.index(key[i])
		c = a-b
		if c<0:
			c += 26
		#find new decrypted letter
		plaintext += letters[c%26]
	return(plaintext)


#open input and key file and read the input and key
input_file = open("input.txt","r")
inp = input_file.readline()

key_file = open("key.txt","r")
key = key_file.readline()

#if key length is less than plaintext then append plaintext as key in existing key
if len(key)<len(inp):
	temp = len(inp)-len(key)
	for i in range(temp):
		key += inp[i]

#now we have key and our plaintext ready for encryption

#let's call encryption function here
cipher = encryption(inp,key)

#create new file and store the result
output = open("output.txt","w")
output.write(cipher)
output.close()

#print the message on console/terminal
print("Encryption done!! check output.txt file\nEnter 1 for Decryption or any other key for exit")
choice = input()

if(choice=="1"):
	#open output file and read the cipher text
	outfile = open("output.txt","r")
	cipher = outfile.readline()

	#call decryption function and store result in plaintext variable
	plaintext = decryption(cipher,key)

	#create input2 file and store the plaintext
	input2 = open("input2.txt","w")
	input2.write(plaintext)
	input2.close()

	#print a message on the terminal
	print("Decryption done!! check the input2.txt file")
input_file.close()
key_file.close()
