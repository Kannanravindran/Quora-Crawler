import networkx as nx
import time
import heapq

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()
dia = nx.diameter(UG)
with open('diameter.txt', mode='wb') as outfile:
	outfile.write('The diameter is: '+str(dia))