import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

'''Page Rank'''
pg_rank = nx.pagerank(G)
top = {}
for x in range(0,10):
	maxx = 0
	for key in pg_rank.keys():
		if pg_rank[key] > maxx:
			maxx = pg_rank[key]
			maxx_key = key
	top[maxx_key] = maxx
	pg_rank[maxx_key] = 0
print top

writer_p = csv.writer(open('pagerank.csv', 'wb'))
for key, value in top.items():
	writer_p.writerow([key,value])

''' eigenvector_centrality'''
eigen_cent = nx.eigenvector_centrality(G)
top = {}
for x in range(0,10):
	maxx = 0
	for key in eigen_cent.keys():
		if eigen_cent[key] > maxx:
			maxx = eigen_cent[key]
			maxx_key = key
	top[maxx_key] = maxx
	print top
	eigen_cent[maxx_key] = 0
writer_e = csv.writer(open('eigen_cent.csv', 'wb'))
for key, value in top.items():
	writer_e.writerow([key,value])

'''degree_centrality'''
deg_cent = nx.degree_centrality(G)
top = {}
for x in range(0,10):
	maxx = 0
	for key in deg_cent.keys():
		if deg_cent[key] > maxx:
			maxx = deg_cent[key]
			maxx_key = key
	top[maxx_key] = maxx
	deg_cent[maxx_key] = 0
print top
writer_d = csv.writer(open('deg_cent.csv', 'wb'))
for key, value in top.items():
	writer_d.writerow([key,value])