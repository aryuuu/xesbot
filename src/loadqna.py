#!/usr/bin/python


#format file qna
#[pertanyaan]?[jawaban]

def load(filename):
	sauce = open(filename).read().split('\n')

	kamus = {} 
	pertanyaan = []
	for i in range(len(sauce)-1): #exclude the last line which is just empty
		pair = sauce[i].split('?') #split q n a
		kamus[pair[0].strip()] = pair[1]
		pertanyaan.append(pair[0].strip())

	return kamus, pertanyaan


# k, p = load("qna")
# print k
# print p

# for q in kamus :
# 	print q, ' >> ', kamus[q]
