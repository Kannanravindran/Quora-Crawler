import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

print UG.size()
small = nx.pappus_graph()
print small.size()

edges = small.edges()
print edges

# with open('small_edges.csv', mode = 'w') as out:
# 	csv_out=csv.writer(out)
# 	for row in edges:
# 		csv_out.writerow(row)
avg_path_len = nx.average_shortest_path_length(small)
print avg_path_len

clust = nx.average_clustering(small)
print clust

with open('small.txt', mode = 'w') as outfile:
	outfile.write('The Average Path Length is: '+str(avg_path_len)+'\nThe Clustering Coefficient is: '+str(clust))