import networkx as nx 
import matplotlib.pyplot as plt


graph=nx.Graph()

graph.add_node(1)
graph.add_node(2)

graph.add_edge(1,2)

nx.draw(graph)

plt.show()