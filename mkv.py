#!/usr/bin/env python

# compares two texts to see how mashupable they are

from __future__ import division
from collections import defaultdict

def createDict(fpath):
	f = open(fpath,'r')
	text = []
	for line in f: 
		text.extend( line.strip("\n").split(" ") )

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

if __name__ == '__main__':
	d1 = createDict('holmes.txt')
	d2 = createDict('styles.txt')
	d3 = createDict('grimms.txt')
	d4 = createDict('holmesreturn.txt')

	s1 = set(d1.keys())
	s2 = set(d2.keys())
	s3 = set(d3.keys())
	s4 = set(d4.keys())

	# what % of all keys do the two texts have in common? 
	# the higher this is, the better the mashup's going to be
	print "Holmes vs. Mystery at Styles", len(s1.intersection(s2)) / len(s1.union(s2))
	print "Holmes vs. Grimms' Tales" ,len(s1.intersection(s3))/ len(s1.union(s3))
	print "Mystery at Styles vs. Grimms'" ,len(s2.intersection(s3))/ len(s2.union(s3))
	print "Holmes vs Holmes", len(s1.intersection(s4))/ len(s1.union(s4))