#Algoritma BM
def BM(text, pattern):
	last = lastOccurrence(pattern);
	n = len(text)
	m = len(pattern)
	i = m-1; # penunjuk indeks pada text

	if (i > n-1):
		#pattern lebih panjang daripada text
		return -1
	else :
		#pattern lebih pendek daripada text
		#mulai penyocokan
		j = m-1 # penunjuk indeks pada pattern
		#cek kecocokan sampai text habis
		while (i <= n-1):
			#character pattern dan text sama, telusuri dari belakang
			#looking-glass technique
			if (pattern[j] == text[i]):
				if (j == 0):
					return i;
				else:
					i = i -1
					j = j -1
			#kalau character tidak sama loncat pengecekan
			#character-jump technique
			else:
				lastOccur = last[ord(text[i])]
				i = i + m -min(j,i+lastOccur)
				j = m-1
		return -1

#fungsi untuk menentukan letak karakter terakhir pada pattern
#dengan index last sebagai ascii dari huruf
#isi last merupakan indeks terakhir huruf ditemukan pada pattern
def lastOccurrence(pattern):
	last = []

	for i in range(128):
		# -1 menandakan huruf tidak ada pada pattern
		last.append(-1)
	for i in range(len(pattern)):
		last[ord(pattern[i])] = i;
	return last

#algoritman BM untuk penyamaan per-kata
def wordsBM(listQnA,pattern):
	listPertanyaan = []
	patternKata = pattern.split(' ')
	prevIdx = -1

	#dilakukan pada seetiap text pada list
	for i in range(len(listQnA)):
		count = 0
		for kata in patternKata:
			idx = BM(listQnA[i],kata)
			#urutan kata pada pattern sesuai dengan urutan kata pada text
			if (idx > prevIdx):
				count += len (kata)
				prevIdx = idx;
		#spasi pada text dianggap tidak ada, karena penyocokan per-kata
		spasiText = len(listQnA[i].split(' ')) -1
		#perhitungan persentase
		persentase = (count/(len(listQnA[i]) - spasiText)) *100
		if (persentase >= 70):
			listPertanyaan.append(listQnA[i])
	return listPertanyaan

#Coba - coba
# print("BM Kalimat")
# text = "Aku hebat sekali"
# pattern = "bat sek"
# x = BM(text, pattern)
# if (x == -1):
# 	print("Sayang sekali, tidak ketemu")
# else:
# 	print("Wahhh, ketemu di " + str(x))
# 	for i in range (len(pattern)):
# 		print(text[i+x], end ="")

# print("BM Kata")
# text = ["Aku a sekali", "Aku bisa tidak dua kali", "Ayo sekali aja"]
# pattern = "Aku sekali"
# x = wordsBM(text, pattern)
# if (len(x) == 0):
# 	print("Sayang sekali, tidak ketemu")
# else:
# 	print("Wahhh, ketemu di " + str(x))
# 	print(x)