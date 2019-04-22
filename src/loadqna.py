#!/usr/bin/python
import KMP as algorithm
import random

#format file qna
#[pertanyaan]?[jawaban]

def load(filename):
	sauce = open(filename).read().split('\n')

	kamus = {} 
	pertanyaan = []
	for i in range(len(sauce)-1): #exclude the last line which is just empty
		pair = sauce[i].split('.') #split q n a
		kamus[pair[0].strip().lower()] = pair[1].lower()
		pertanyaan.append(pair[0].strip().lower())

	return kamus, pertanyaan




