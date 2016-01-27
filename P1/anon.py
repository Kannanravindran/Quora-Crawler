import csv
from compiler.ast import flatten

anon=1
with open('crappy.csv', mode='r') as infile:
	reader = csv.reader(infile)
	mydict = dict((rows[0],rows[1]) for rows in reader)
newdict = {}
anondict = {}
anonlist = []
#flat = flatten(mydict.values())
for key in mydict.keys():
	newdict[key] = anon
	anon+=1
iteration=0
nd = {}
for key, val in mydict.items():
	v = val.strip('[').strip(']').split(',')
	nd[key] = v
flat = flatten(nd.values())
for x in flat:
	if x not in newdict:
		newdict[x] = anon
		anon+=1
#print flat
#print newdict
#print len(flat)

writer = csv.writer(open('map.csv', 'wb'))
for key, value in newdict.items():
	writer.writerow([key,value])
########################################
for key in mydict.keys():
	for keyy,vall in newdict.items():
		for values in mydict[key].strip('[').strip(']').split(','):
			if values == keyy:
				anonlist.append(newdict[keyy])
		if key==keyy:			 #iterate the values in the dictionary
			anondict[newdict[keyy]]=anonlist
			anonlist = []
	iteration+=1
	print iteration,' : ', key

writer = csv.writer(open('ANONUSERS.csv', 'w'))
for key, value in anondict.items():
	writer.writerow([key,value])