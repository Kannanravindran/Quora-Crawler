import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()
clust_global = nx.average_clustering(UG)
#print 'Average Global Clustering Coefficient: ',avg_clust_local
avg_clust_local = nx.clustering(UG)
#print 'Local Clustering Coefficient: ',clust_global

writer = csv.writer(open('avg_clust.csv', 'wb'))
for key, value in avg_clust_local.items():
	writer.writerow([key,value])

with open('clust_global.txt', mode='wb') as outfile:
	outfile.write('Global Clustering Coefficient: '+str(clust_global))