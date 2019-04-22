#!/usr/bin/python
from flask import Flask, request, render_template
import KMP
from BM import *
from REGEX import REGEX
import loadqna
from sanitize import sanitize

# load database pertanyaan dan jawaban
kamus, lisp = loadqna.load("qna")






app = Flask(__name__)

#home page
@app.route('/')
@app.route('/index')
@app.route('/<page>')
def home(page=None):
	if(page):
		return render_template('php/'+page+'.php')
	else:
		return render_template('php/index.php')

#kmp page
@app.route('/kmp', methods=['POST'])
def getkmp():
	# list untuk menyimpan pertanyaan yang mirip
	listPertanyaan = []
	listKataSama = []
	result = ''

	#terima input user dan bersihkan dari dari stop word dan 
	#ganti kata kata di dalamnya dengan sinonim yang terdapat 
	#dalam database
	pertanyaan = sanitize(request.form['text']).lower()
	# cek keseluruhan kalimat terlebih dahulu
	for i in range(len(lisp)):
		idx = KMP.KMP(lisp[i], pertanyaan)
		if(idx != -1):
			listPertanyaan.append(lisp[i])

	# cek kecocokan berdasarkan kata per kata dari input user jika tidak ada kata yang sama persis
	if(len(listPertanyaan) == 0):
		kalimat = pertanyaan.split(' ')
		prevIdx = -1
		for i in range(len(lisp)):
			for kata in kalimat:
				idx = KMP.KMP(lisp[i], kata)
				if (idx > prevIdx):
					listKataSama.append(kata)
					prevIdx = idx

			# hitung jumlah kata yang sama
			count = 0
			for kata in listKataSama:
				count += len(kata)
			
			count += len(kalimat) - 1 
			# apakah kata sudah mirip >= 80% jika ya masukkan ke list pertanyaan
			persentase = count/len(lisp[i]) * 100
			if(persentase >= 80):
				listPertanyaan.append(lisp[i])

	# keluarkan jawaban dari bot
	if(len(listPertanyaan) == 0):
		# print("Can you ask other question ?")
		result = "Can you ask another question?"
	else:
		# if(len(listPertanyaan) == 1):
			# print(k[listPertanyaan[0]])
		result = kamus[listPertanyaan[0]]
		# # lebih dari 1 yang mirip keluarkan jawaban random dari listPertanyaan yang terpilih
		# else:
		# 	idx = random.randint(0, len(listPertanyaan))
		# 	print("xesbot : " + kamus[listPertanyaan[idx]])

	return render_template('php/kmp.php', answer=result, quest=pertanyaan)

#bm page
@app.route('/bm', methods=['POST'])
def getbm():
	pertanyaan = sanitize(request.form['text']).lower()
	result = -1
	i = 0
	while (i < len(lisp) and result < 0):
		result = BM(lisp[i], pertanyaan)
		i += 1
	if (result < 0):
		result = wordsBM(lisp,pertanyaan)
		if (len(result)>0):
			pertanyaan = result[0]
			i = 0
			result = -1
			while (i < len(lisp) and result < 0):
				result = BM(lisp[i],pertanyaan)
				i += 1
			result = kamus[lisp[i]]
		else:
			# print("Can you ask other question ?")
			result = "Can you ask another question?"
	else:
		result = kamus[lisp[i-1]]

	return render_template('php/bm.php', answer=result, quest=pertanyaan)

#regex page
@app.route('/regex', methods=['POST'])
def getregex():
	pertanyaan = sanitize(request.form['text']).lower()
	# pertanyaan = request.form['text']
	result = []
	i = 0
	while(i < len(lisp) and not result): #periksa apakah pertanyaan
		result = REGEX(lisp[i], pertanyaan)
		i += 1

	if(result):
		result = kamus[''.join(result)+'?']
	else:
		result = "Can you ask another question?"


	return render_template('php/regex.php', answer=result, quest=pertanyaan)


if(__name__ == '__main__'):
	app.run(debug=True)
# #terima input user dan bersihkan dari dari stop word dan 
# #ganti kata kata di dalamnya dengan sinonim yang terdapat 
# #dalam database
# pertanyaan = sanitize(raw_input())

# #baca jenis algoritma string matching yang diinginkan user
# algo = raw_input()

# if(algo == "KMP"):
# 	# cek keseluruhan kalimat terlebih dahulu
# 	for i in range(len(lisp)):
# 		idx = KMP.KMP(lisp[i], pertanyaan)
# 		if(idx != -1):
# 			listPertanyaan.append(lisp[i])

# 	# cek kecocokan berdasarkan kata per kata dari input user jika tidak ada kata yang sama persis
# 	if(len(listPertanyaan) == 0):
# 		kalimat = pertanyaan.split(' ')
# 		prevIdx = -1
# 		for i in range(len(lisp)):
# 			for kata in kalimat:
# 				idx = KMP.KMP(lisp[i], kata)
# 				if (idx > prevIdx):
# 					listKataSama.append(kata)
# 					prevIdx = idx

# 			# hitung jumlah kata yang sama
# 			count = 0
# 			for kata in listKataSama:
# 				count += len(kata)
			
# 			count += len(kalimat) - 1 
# 			# apakah kata sudah mirip >= 80% jika ya masukkan ke list pertanyaan
# 			persentase = count/len(p[i]) * 100
# 			if(persentase >= 80):
# 				listPertanyaan.append(p[i])

# 	# keluarkan jawaban dari bot
# 	if(len(listPertanyaan) == 0):
# 		print("Can you ask another question ?")
# 	else:
# 		if(len(listPertanyaan) == 1):
# 			print(k[listPertanyaan[0]])
# 		# lebih dari 1 yang mirip keluarkan jawaban random dari listPertanyaan yang terpilih
# 		else:
# 			idx = random.randint(0, len(listPertanyaan))
# 			print("xesbot : " + k[listPertanyaan[idx]])

# elif(algo == "BM"):
# 	result = -1
# 	i = 0
# 	while (i < len(lisp) and result < 0):
# 		result = BM(lisp[i], pertanyaan)
# 		i += 1
# 	if (result < 0):
# 		result = WordsBM(lisp,pertanyaan)
# 		if (len(result)>0):
# 			pertanyaan = result[0]
# 			i = 0
# 			result = -1
# 			while (i < len(lisp) and result < 0):
# 				result = BM(lisp[i],pertanyaan)
# 				i += 1
# 			result = kamus[i]
# 		else:
# 			print("Can you ask another question ?")
# 	else:
# 		result = kamus[i]

# elif(algo == "REGEX"):
# 	result = []
# 	i = 0
# 	while(!result): #periksa apakah pertanyaan
# 		result = REGEX(pertanyaan, lisp)
# 		i += 1

# 	if(result):
# 		result = kamus[result]
# 	else:
# 		print "dude what"

# else:
# 	print "Maaf algoritma tidak tersedia"
