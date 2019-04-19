#!/usr/bin/python
import sys

#mengembalikan dictionary berupa pasangan kata dan sinonimnya
def load(filename):
	sauce = open("sinonim").read().split('\n')

	#dictionary dengan key berupa kata-kata yang tidak terdapat pada daftar
	#pertanyaan, dan value berupa kata-kata yang terdapat pada daftar pertanyaan.
	dsinonim = {}

	for line in sauce:
		dsinonim[line.split('|')[0]] = line.split('|')[-1]

	return dsinonim

#menambahkan pasangan key dan value baru pada dict
#dan menuliskan ke dalam file
def write(filename):
	sauce = open(filename, "a+")

	k = ""
	v = ""
	while(k != "///"):
		k = raw_input("kata	: ")
		v = raw_input("Sinonim 	: ")

		if(k != "///"):
			line = k + "|" + v + "\n"
			sauce.write(line)
	sauce.close()

	

# main
# if(len(sys.argv) < 3):
# 	print "usage : ./sinonim [w|l] [filename]"
# else:
# 	if(sys.argv[1] == 'w'):
# 		write(sys.argv[2])
# 	elif(sys.argv[1] == 'l'):
# 		kamus = load(sys.argv[2])
# 		print kamus
# 	else:
# 		print "usage : ./sinonim [w|l] [filename]"
