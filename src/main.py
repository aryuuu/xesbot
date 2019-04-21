import KMP
import BM
from REGEX import REGEX
import loadqna
from sanitize import sanitize

#load database pertanyaan dan jawaban
kamus, lisp = loadqna.load("qna")






#terima input user dan bersihkan dari dari stop word dan 
#ganti kata kata di dalamnya dengan sinonim yang terdapat 
#dalam database
pertanyaan = sanitize(raw_input())

#baca jenis algoritma string matching yang diinginkan user
algo = raw_input()

if(algo == "KMP"):
	
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
			print("Can you ask other question.")
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
