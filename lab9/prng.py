#Psuedo Random Number Generator

#load input file and read the 6bit input
input_file = open("input.txt","r")
inp = int(input_file.readline())

arr = []  #arr is the list contaning 6 input bits
#read 6 bits from input number
for i in range(6):
    arr.append(inp&1)
    inp=inp>>1
arr.reverse()
#function to calculate power
def power(a,b):
    ans = 1
    while b>0:
        ans *= a
        b -= 1
    return(ans)

#function to calculate decimal form
def decimal(num):
    ans = 0
    count=5
    for i in range(6):
        ans += num[i]*power(2,count)
        count -= 1
    return(ans)

#function to generate random number from [1,63]
def prng():
    global arr
    #calculate new rightmost bit as A
    A = arr[1]^arr[3]
    #shift all bits
    for i in range(5):
        arr[i]=arr[i+1]
    #set A as rightmost bit
    arr[5] = A
    #calculate decimal number from [1,63] using arr
    return(decimal(arr)%63+1)
#generate first random number and store it to later check for repition
out = open("output.txt","w")
num = prng()
out.write(str(num)+"\n")

#generate new random numbers untill first one come again
n = prng()
while n!=num:
    out.write(str(n)+"\n")
    n=prng()
#print a message on the terminal
print("Done!! check output.txt file for new sequence try with new number in input.txt")
input_file.close()
out.close()