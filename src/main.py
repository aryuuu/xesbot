import KMP
import BM
from REGEX import REGEX
import loadqna
from sanitize import sanitize

# load database pertanyaan dan jawaban
kamus, lisp = loadqna.load("qna")

# list untuk menyimpan pertanyaan yang mirip
listPertanyaan = []
listKataSama = []

#terima input user dan bersihkan dari dari stop word dan 
#ganti kata kata di dalamnya dengan sinonim yang terdapat 
#dalam database
pertanyaan = sanitize(raw_input())

#baca jenis algoritma string matching yang diinginkan user
algo = raw_input()

if(algo == "KMP"):
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
			persentase = count/len(p[i]) * 100
			if(persentase >= 80):
				listPertanyaan.append(p[i])

	# keluarkan jawaban dari bot
	if(len(listPertanyaan) == 0):
		print("Can you ask other question ?")
	else:
		if(len(listPertanyaan) == 1):
			print(k[listPertanyaan[0]])
		# lebih dari 1 yang mirip keluarkan jawaban random dari listPertanyaan yang terpilih
		else:
			idx = random.randint(0, len(listPertanyaan))
			print("xesbot : " + k[listPertanyaan[idx]])

elif(algo == "BM"):
	result = -1
	i = 0
	while (i < len(lisp) and result < 0):
		result = BM(lisp[i], pertanyaan)
		i += 1
	if (result < 0):
		result = WordsBM(lisp,pertanyaan)
		if (len(result)>0):
			pertanyaan = result[0]
			i = 0
			result = -1
			while (i < len(lisp) and result < 0):
				result = BM(lisp[i],pertanyaan)
				i += 1
			result = kamus[i]
		else:
			print("Can you ask other question ?")
	else:
		result = kamus[i]

elif(algo == "REGEX"):
	result = []
	i = 0
	while(!result): #periksa apakah pertanyaan
		result = REGEX(pertanyaan, lisp)
		i += 1

	if(result):
		result = kamus[result]
	else:
		print "dude what"

else:
	print "Maaf algoritma tidak tersedia"
