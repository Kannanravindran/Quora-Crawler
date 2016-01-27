import snap
Graph = snap.LoadEdgeList(snap.PUNGraph, "edgeListKannan.txt", 0, 1)
    x = 0
    V = snap.TIntPrV()
    snap.GetEdgeBridges(Graph, V)
    for e in V:
        x+=1
    print 'Bridges: ', x, '\n'