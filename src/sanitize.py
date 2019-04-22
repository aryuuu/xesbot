#!/usr/bin/python
import sinonim

ksin = sinonim.load("sinonim")
kstop = open("stopper").read().split('\n')

#membersihkan sentence dari stopper word
def clearstopper(sentence):
	result = ""
	for i in sentence.split(' '):
		if(i not in kstop):
			result += i
			result += ' '

	return result.strip()

#mengganti kata kata yang terdapat dalam sentence dan
#menggantinya dengan sinonim yang terdapat daftar sinonim
def formalize(sentence):
	result = ""
	for i in sentence.split(' '):
		if(i in ksin):
			result += ksin[i]
		else:
			result += i
		result += ' '


	return result.strip()

#mengembalikan sentence yang sudah bersih dari stopper word
#dan seluruh kata kata di dalamnya sudah diganti diganti dengan
#sinonimnya
def sanitize(sentence):
	return formalize(clearstopper(sentence))

