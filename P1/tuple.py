import csv

with open('ANONUSERS.csv', mode='r') as infile:
	reader = csv.reader(infile)
	mydict = dict((rows[0],rows[1]) for rows in reader)

usertup = ()
userlist = []
count = 0
#userlist = tuple(mydict.items())
'''nd = {}
for key, val in mydict.items():
	v = val.strip('[').strip(']').split(',')
	nd[key] = v
	for x in nd[key]:
		usertup = (key,x)
		userlist.append(usertup)
		count+=1'''

writer = csv.writer(open('U_tuples.csv', 'a'),delimiter = ',')
for key, val in mydict.items():
	v1 = val.strip('[').strip(']').split(',')
	for v in v1:
		#print key,v
		writer.writerow([key,v])
	count+=1
#usertup = usertup.split('","')
#print userlist
	print count
#writer = csv.writer(open('U_tuples.txt', 'wb'))
#writer.writerow(userlist)