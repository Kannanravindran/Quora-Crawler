import networkx as nx
import csv

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

print UG.size()
nodes = len(UG)
prob = 0.00008015591 #UG.size()/(nodes*(nodes-1))
print prob
rand = nx.connected_watts_strogatz_graph(nodes,20,prob,tries = 100000000 ,seed = None)
print rand.size()


edges = rand.edges()
len(edges)

# with open('rand_edges.csv', mode = 'w') as out:
# 	csv_out=csv.writer(out)
# 	for row in edges:
# 		csv_out.writerow(row)
avg_path_len = nx.average_shortest_path_length(rand)
print avg_path_len

clust = nx.average_clustering(rand)
print clust