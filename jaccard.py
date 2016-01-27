import networkx as nx
import heapq

with open('U_tuples.csv', mode='r') as infile:
	G = nx.read_edgelist(infile, delimiter = ',', create_using=nx.DiGraph())
UG = G.to_undirected()
preds = nx.jaccard_coefficient(UG)
nd = {}
count = 0
check = 10000

def jac_check():
	ndmax = heapq.nlargest(1,nd,nd.get)
	if nd[ndmax[0]] == 1:
		with open('jaccard.txt', mode='wb') as outfile:
			outfile.write("Jaccard Similarity Pair:	"+str(ndmax)+"\n")
			outfile.write("Jaccard Similarity Maximum:	"+str(nd[ndmax[0]])+"\n")

for u,v,p in preds:
	nd[(u,v)] = p
	count+=1
	print 'Jaccard: ' ,count 
	ndmax = []
	if count == check:
		jac_check()
		check += 10000+count
print nd

#ndmax = []
#ndmax = heapq.nlargest(1,nd,nd.get)
#print ndmax
#writer = csv.writer(open('jaccard_output.txt', 'wb'))
#writer.write("Jaccard Similarity Pair:	"+str(ndmax)+"\n")
#writer.write("Jaccard Similarity Maximum:	"+str(nd[ndmax[0]])+"\n")