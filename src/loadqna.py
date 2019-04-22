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
		kamus[pair[0].strip('?').lower()] = pair[1].lower()
		pertanyaan.append(pair[0].strip().lower())

	return kamus, pertanyaan


# k, p = load("qna")
# q = []
# print("Halo ini xesbot, Apakah ada yang bisa dibantu ?")
# q = input("You : ").lower()

# kalimat = q.split(' ')
# listKataSama = []
# listPertanyaan = []

# # cek keseluruhan kalimat
# for i in range(len(p)):
# 	idx = algorithm.KMP(p[i], q)
# 	if (idx != -1):
# 		listPertanyaan.append(p[i])

# # cek kecocokan berdasarkan kata per kata dari input user jika tidak ada kata yang sama persis
# if(len(listPertanyaan) == 0):
# 	prevIdx = -1
# 	for i in range(len(p)):
# 		for kata in kalimat:
# 			idx = algorithm.KMP(p[i], kata)
# 			if (idx > prevIdx):
# 				listKataSama.append(kata)
# 				prevIdx = idx

# 		# hitung jumlah kata yang sama
# 		count = 0
# 		for kata in listKataSama:
# 			count += len(kata)
		
# 		count += len(kalimat) - 1 
# 		# apakah kata sudah mirip >= 80% jika ya masukkan ke list pertanyaan
# 		persentase = count/len(p[i]) * 100
# 		if(persentase >= 80):
# 			listPertanyaan.append(p[i])

# # keluarkan jawaban dari bot
# if(len(listPertanyaan) == 0):
# 	print("xesbot : Apakah ada pertanyaan lain ?")
# else:
# 	if(len(listPertanyaan) == 1):
# 		print("xesbot : " +  k[listPertanyaan[0]])
# 	# lebih dari 1 yang mirip keluarkan jawaban random dari listPertanyaan yang terpilih
# 	else:
# 		idx = random.randint(0, len(listPertanyaan))
# 		print("xesbot : " + k[listPertanyaan[idx]])



