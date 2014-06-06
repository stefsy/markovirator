#!/usr/bin/env python

# compares two texts to see how mashupable they are

# next! remove quotation marks, put periods semicolonsand commas into key value

from __future__ import division
from collections import defaultdict
from nltk.collocations import *

import sys
import nltk
import timeit
import random

def createDict(fpath):
	f = open(fpath,'r')
	text = []
	for line in f: 
		# text.extend( line.rstrip("\n").rstrip("\r").strip('\"').split(" ") )
		# nltk for the save
		text.extend(nltk.tokenize.wordpunct_tokenize(line))
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

def mergeTexts(listLookups):
	mergedLookup = defaultdict(list)
	for lookup in listLookups:
		for k, v in lookup.items():
			mergedLookup[k].extend(v)
	return mergedLookup

# flesh out later
def checkDict(d):
	kError = 0
	k = []
	for k in d.keys():
		if len(k) != 2:
			kError+=1
			k.append(k)
	print kError

def writeNew(chain,nWords):
	#pick the most common key as the first two words
	key = max(chain.iterkeys(), key=(lambda key: len(chain[key])))
	val = random.choice(chain[key])
	wc = 3
	newText = key[0] + " " + key[1] + " " + val

	#keep adding new words, if key not found, select random word
	#could be cleaned up, type checking feels awkward
	while wc < nWords:
		key = (key[1],val)
		if key in chain: 	
			val = random.choice(chain[key]) 
		else: 
			# if only one possible value, output is string, else is a list of strs
			r = random.choice(chain.values())
			if type(r) is str:
				val = r
			else:
				val = random.choice(r)
		newText+= " " + val		
		wc+=1 
	return newText

if __name__ == '__main__':

	lookups = []
	for i in range(1,len(sys.argv)-1):
		lookups.append(createDict(sys.argv[i]))

	# 1, the setup required to run timeit on custom defined funtions is too much
	# 2, createDict() takes about 2.1s to run on a 595kb text file
	# print(timeit.timeit("createDict('holmes.txt')", setup="from __main__ import createDict",number=50))	
	
	#write 200 words of the new mashup
	mashup = mergeTexts(lookups)
	print writeNew(mashup,100)

	# what % of all keys do the two texts have in common? 
	# # the higher this is, the better the mashup's going to be

	# s1 = set(d1.keys())
	# s2 = set(d2.keys())
	# s3 = set(d3.keys())
	# s4 = set(d4.keys())

	# print "The Fairy Tales of Sherlock Holmes"
	# print "Mashup Rating:", len(s1.intersection(s3)) / len(s1.union(s3))
	# print "Holmes vs. Grimms' Tales" ,len(s1.intersection(s3))/ len(s1.union(s3))
	# print "Mystery at Styles vs. Grimms'" ,len(s2.intersection(s3))/ len(s2.union(s3))
	# print "Holmes vs Holmes", len(s1.intersection(s4))/ len(s1.union(s4))


	
