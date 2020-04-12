import string
lower = string.ascii_lowercase
dia = ["th", "er","on", "an", "re", "he", "in", "ed", "nd", "ha", "at", "en", "es", "of", "or", "nt", "ea", "ti", "to", "it", "st", "io", "le", "is", "ou", "ar", "as", "de", "rt", "ve"]
two = ["of", "to", "in", "it", "is", "be", "as", "at", "so", "we", "he", "by", "or", "on", "do", "if", "me", "my", "up", "an", "go", "no", "us", "am"]
three  = ["the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had", "her", "was", "one", "our", "out", "day", "get", "has", "him", "his", "how", "man", "new", "now", "old", "see", "two", "way", "who", "boy", "did", "its", "let", "put", "say", "she", "too", "use"]
four = ["that", "with", "have", "this", "will", "your", "from", "they", "know", "want", "been", "good", "much", "some", "time"]


def con(n):
	if n<0:
		return(26+n)
	else:
		return n
def dec(s,k):
	ans = ""
	for i in range(len(s)):
		ind = lower.index(s[i])
		ans += lower[con(ind-k)]
	return(ans)
def checkfour(s):
	i1 = lower.index(s[0])
	i2 = lower.index(s[1])
	i3 = lower.index(s[2])
	i4 = lower.index(s[3])
	for i in range(len(four)):
		d1 = lower.index(four[i][0])
		d2 = lower.index(four[i][1])
		d3 = lower.index(four[i][2])
		d4 = lower.index(four[i][3])
		if con(d1-d2)==con(i1-i2) and con(d2-d3)==con(i2-i3) and con(d3-d4)==con(i3-i4):
			return(max(d1-i1,i1-d1))
	return(0)

def checkthree(s):
	i1 = lower.index(s[0])
	i2 = lower.index(s[1])
	i3 = lower.index(s[2])
	for i in range(len(three)):
		d1 = lower.index(three[i][0])
		d2 = lower.index(three[i][1])
		d3 = lower.index(three[i][2])
		if con(d1-d2)==con(i1-i2) and con(d2-d3)==con(i2-i3) and con(d1-d3)==con(i1-i3):
			return(max(d1-i1,i1-d1))
	return(0)

def checktwo(s):
	i1 = lower.index(s[0])
	i2 = lower.index(s[1])
	for i in range(len(two)):
		d1 = lower.index(two[i][0])
		d2 = lower.index(two[i][1])
		if con(d1-d2)==con(i1-i2):
			return(max(d1-i1,i1-d1))
	return(0)

o = open("outputt.txt","r")
c = list(o.readline().split())
key = 0
for i in range(len(c)):
	if len(c[i])==2:
		flag = checktwo(c[i])
	elif len(c[i])==3:
		flag = checkthree(c[i])
	elif len(c[i])==4:
		flag = checkfour(c[i])
	if flag:
		key=flag
		break
if key>10:
	key = 26-key
ans = str(key)+"\n"
for i in range(len(c)):
	c[i] = dec(c[i],key)
	ans += c[i]
	ans += " "
out = open("inputt.txt","w")
out.write(ans)
