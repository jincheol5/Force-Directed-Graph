import networkx as nx 
import matplotlib.pyplot as plt
from kamada_kawai import get_d,get_l



#create graph 
graph=nx.Graph()


nodes=['a','b','c','d','e']
weighted_edges=[('a','b',1),('a','c',1),('a','e',1)
    ,('b','e',1),('b','c',1),('b','d',1),('e','d',1),('c','d',1)]


graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(weighted_edges)











pos=nx.kamada_kawai_layout(graph)

nx.draw(graph,pos,with_labels=True)

plt.show()



