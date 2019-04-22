#!/usr/bin/python

#jalankan program dan isi pertanyaan dan jawaban untuk melangkapi koleksi qna 

sauce = open("qna", "a+")

q = ""
a = ""
while(q != "end"):
	q = input("pertanyaan	: ")
	a = input("jawaban 	: ")

	if(q != "end"):
		line = q + "." + a + "\n"
		sauce.write(line)

sauce.close()