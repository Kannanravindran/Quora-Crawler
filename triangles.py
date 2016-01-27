import networkx as nx
import time

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()

cycle_UG = {}
count = 0

cycle_UG = nx.triangles(UG)
for key in cycle_UG.keys():
	count+=1
with open('triangles.txt', mode = 'wb') as outfile:
	outfile.write('Number of 3 cycles are: '+str(count))