import snap

snapPA = snap.LoadEdgeList(snap.PUNGraph, 'rand.txt', 0, 1)
snapPAedges = snapPA.Edges()
snap.PlotInDegDistr(snapPA, "Random", "Undirected graph - degree Distribution",'True','True')
snapPA = snap.LoadEdgeList(snap.PUNGraph, 'small.txt', 0, 1)
snapPAedges = snapPA.Edges()
snap.PlotInDegDistr(snapPA, "Small", "Undirected graph - degree Distribution",'True','True')
snapPA = snap.LoadEdgeList(snap.PUNGraph, 'pref.txt', 0, 1)
snapPAedges = snapPA.Edges()
snap.PlotInDegDistr(snapPA, "Preferential", "Undirected graph - degree Distribution",'True','True')