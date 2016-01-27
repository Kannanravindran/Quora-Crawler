import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

print UG.size()

avg_path_len = nx.average_shortest_path_length(UG)
print avg_path_len

clust = nx.average_clustering(UG)
print clust

with open('realworld.txt', mode = 'w') as outfile:
	outfile.write('The Average Path Length is: '+str(avg_path_len)+'\nThe Clustering Coefficient is: '+str(clust))