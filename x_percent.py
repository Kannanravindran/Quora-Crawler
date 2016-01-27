import networkx as nx
import csv

for xp in range(1,101):
	with open('U_tuples.csv', mode='r') as infile: 
		reader = csv.reader(infile)
		edgelist = list((rows[0],rows[1]) for rows in reader)
	rand = (int)(len(edgelist)*(0.01*xp))
	for x in range(0,rand):
		edgelist.pop()
	with open('U_tuples_reduced.csv', mode = 'w') as out:
		csv_out=csv.writer(out)
		for row in edgelist:
			csv_out.writerow(row)

	with open('U_tuples_reduced.csv', mode='r') as w_infile:
		G = nx.read_edgelist(w_infile, delimiter = ',', create_using=nx.DiGraph())
	UG = G.to_undirected()

	conn_comp = []
	conn_comp = nx.connected_components(UG)
	maxx = 0
	for x in conn_comp:
		if len(x) > maxx:
			maxx = len(x)
	print xp
	with open('x_percent.txt', mode = 'a') as outfile:
		outfile.write('Edgesreduced = '+str(xp)+'% \tConnected component max = '+str(maxx)+'\n')