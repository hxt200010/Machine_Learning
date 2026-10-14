import networkx as nx
G=nx.Graph()
G.add_edges_from([('a','b'),('b','c'),('c','d'),('b','d')])
print('Number of nodes:',G.number_of_nodes())
print('Node degree dictionary:',dict(G.degree()))
print('Most connected node:',max(G.degree,key=lambda item:item[1])[0])
