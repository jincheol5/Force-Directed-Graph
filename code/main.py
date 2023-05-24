import networkx as nx 
import matplotlib.pyplot as plt
import kamada_kawai as kk
from graph import Graph



#빈 figure 생성
fig = plt.figure()

display_size=fig.get_size_inches()
display_width=display_size[0]



#create graph
#precondition : connected graph  
graph=nx.Graph()


nodes=['a','b','c','d','e','f']
weighted_edges=[
    ('a','b',1),('a','e',1)
    ,('b','a',1),('b','d',1),('b','e',1)
    ,('c','d',1),('c','f',1)
    ,('d','b',1),('d','c',1),('d','f',1)
    ,('e','a',1),('e','b',1)
    ,('f','c',1),('f','d',1)
    ]


graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(weighted_edges)


pos=nx.shell_layout(graph) #shell layout으로 초기화 
#pos=nx.kamada_kawai_layout(graph)



#set graph to Graph class 
G=Graph(graph)


G=kk.update_algorithm(G,pos,display_width,e=0.3)

#nx.draw(G.graph,pos,with_labels=True)
nx.draw(G.graph,G.pos,with_labels=True)

plt.show()



