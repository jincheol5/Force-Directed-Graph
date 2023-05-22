import networkx as nx 
import matplotlib.pyplot as plt

def get_d(graph): #d_ij = pi 와 pj의 최단거리 
    
    d_dic={}
    
    nodes=graph.nodes
    
    
    for source in nodes:
        shortest_distance={}
        for target in nodes:
            if nx.has_path(graph,source,target) and (source!=target):
                shortest_distance[target]=nx.shortest_path_length(graph,source,target)
        
        d_dic[source]=shortest_distance      

    return d_dic


def get_L(graph,display_length):
    
    diameter=nx.diameter(graph)
    
    return display_length/diameter

    
def get_l(graph,display_length):
    
    l_dic={} #key = source, value = 각 target에 대한 l dic 
    
    L=get_L(graph,display_length)
    
    for source in graph.nodes:
        target_dic={}
        for target in graph.nodes:
            if nx.has_path(graph,source,target) and (source!=target):
                d=nx.shortest_path_length(graph,source,target)
                target_dic[target]=L*d
        l_dic[source]=target_dic
        
        
    return l_dic


def get_k(graph,K): #k = spring의 힘 , K = 상수 
    
    k_dic={}
    
    return k_dic
    
    