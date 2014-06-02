#!/usr/bin/env python

# compares two texts to see how mashupable they are

# next! remove quotation marks, put periods semicolonsand commas into key value

from __future__ import division
from collections import defaultdict
import timeit
import random


def createDict(fpath):
	f = open(fpath,'r')
	text = []
	for line in f: 
		text.extend( line.rstrip("\n").rstrip("\r").strip('\"').split(" ") )
 	text = filter(None,text) #remove blanks

	d = defaultdict(list)
	for i in range(0,len(text)): 
		try:
			k = (text[i], text[i+1])
			v = text[i+2]
			#defaultdict creates entry automatically if not in the mapping
			d[k].append(v)
		except IndexError:
			pass
	return d

def mergeTexts(d1,d2):
	mergedDict = d1
	for k, v in d2:
		mergedDict[k].append(v)
	return mergedDict

#test function, flesh out laster
def checkDict(d):
	for k in d:
		if len(k) != 2:
			print k
			break

def writeNew(chain,nWords):
	#pick the most common key as the first two words
	key = random.choice(chain.keys())
	val = chain[key][0]
	wc = 3
	newText = key[0] + " " + key[1] + " " + val

	#keep adding new words, if key not found, select random word
	#could be cleaned up, type checking seems like it can be removed
	while wc < nWords:
		key = (key[1],val)
		if key in chain: 	
			val = random.choice(chain[key]) 
		else: 
			r = random.choice(chain.values())
			if type(r) is str:
				val = r
			else:
				val = random.choice(r)
		newText+= " " + val		
		wc+=1 
	return newText


if __name__ == '__main__':

	d1 = createDict('holmes.txt')
	d2 = createDict('styles.txt')
	# d3 = createDict('grimms.txt')
	# d4 = createDict('holmesreturn.txt')

	s1 = set(d1.keys())
	s2 = set(d2.keys())
	# s3 = set(d3.keys())
	# s4 = set(d4.keys())

	# 1, the setup required to run timeit on custom defined funtions is stupid
	# 2, createDict() takes about 2.2s to run on a 595kb text file
	# print(timeit.timeit("createDict('holmes.txt')", setup="from __main__ import createDict",number=10))	
	
	# what % of all keys do the two texts have in common? 
	# # the higher this is, the better the mashup's going to be

	print "Holmes vs. Mystery at Styles", len(s1.intersection(s2)) / len(s1.union(s2))
	# print "Holmes vs. Grimms' Tales" ,len(s1.intersection(s3))/ len(s1.union(s3))
	# print "Mystery at Styles vs. Grimms'" ,len(s2.intersection(s3))/ len(s2.union(s3))
	# print "Holmes vs Holmes", len(s1.intersection(s4))/ len(s1.union(s4))

	# checkDict(d1)

	#write 200 words of the new mashup
	mashup = mergeTexts(d1,d2)
	print writeNew(mashup,200)