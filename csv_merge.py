import csv
with open('out.csv', mode='r') as infile1:
	reader = csv.reader(infile1)
	mydict1 = dict((rows[0],rows[1]) for rows in reader)
#with open('users_test.csv', mode='r') as infile2:
#	reader = csv.reader(infile2)
#	mydict2 = dict((rows[0],rows[1]) for rows in reader)
with open('crappy.csv', mode='r') as infile3:
	reader = csv.reader(infile3)
	mydict3 = dict((rows[0],rows[1]) for rows in reader)
#with open('users_250.csv', mode='r') as infile4:
#	reader = csv.reader(infile4)
#	mydict4 = dict((rows[0],rows[1]) for rows in reader)
z = {}
z = mydict3.copy()
z.update(mydict1)
#z.update(mydict3)
#z.update(mydict4)

with open('crappy.csv', mode='wb') as outfile:
	writer = csv.writer(outfile)
	for key, value in z.items():
		writer.writerow([key,value])