import loadqna

k, p = loadqna.load("qna")

for i in p:
	print i 

for i in k:
	print i, k[i]