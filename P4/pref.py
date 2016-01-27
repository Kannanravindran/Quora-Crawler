import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

m = UG.size()
n = len(UG)
pref = nx.barabasi_albert_graph(n,((2*m)/n))
print pref.size()


avg_path_len = nx.average_shortest_path_length(pref)

clust = nx.average_clustering(pref)

with open('preferential.txt', mode = 'w') as outfile:
	outfile.write('The Average Path Length is: '+str(avg_path_len)+'\nThe Clustering Coefficient is: '+str(clust))