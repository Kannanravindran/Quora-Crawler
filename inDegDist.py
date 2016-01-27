import networkx as nx
import matplotlib.pyplot as plt

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())

UG = G.to_undirected()
print len(G.nodes()),len(G.edges())
degree_sequence=sorted(G.out_degree().values(),reverse=True)
plt.loglog(degree_sequence,'b-',marker='o')
plt.show()

in_deg = sorted(G.in_degree().values(),reverse=True)
plt.loglog(in_deg, 'b-', marker ='o')
plt.show()