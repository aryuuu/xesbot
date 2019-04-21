#!/usr/bin/python
import re

#fungsi ini mengembalikan text yang memenuhi pattern jika ditemukan 
def REGEX(text, pattern):
	pattern = pattern.split(' ')
	pattern = '.*'.join(pattern)
	result = re.findall(pattern, text)

	return result



