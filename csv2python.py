import csv

with open('crappy.csv', mode='r') as infile:
	reader = csv.reader(infile)
	mydict = dict((rows[0],rows[1]) for rows in reader)
with open('save.py', mode='wb') as outfile:
	outfile.write("d="+str(mydict))