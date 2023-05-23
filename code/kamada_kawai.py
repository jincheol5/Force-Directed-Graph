import networkx as nx 
import matplotlib.pyplot as plt
import math

def get_d(graph): #d_ij = pi 와 pj의 최단거리 
    
    d_dic={}
    
    nodes=graph.graph.nodes
    
    
    for source in nodes:
        shortest_distance={}
        for target in nodes:
            if nx.has_path(graph.graph,source,target) and (source!=target):
                shortest_distance[target]=nx.shortest_path_length(graph.graph,source,target)
            else:
                shortest_distance[target]=0
        d_dic[source]=shortest_distance      

    return d_dic


def get_L(graph,display_length):
    
    diameter=nx.diameter(graph.graph)
    
    return display_length/diameter

    
def get_l(graph,display_length):
    
    l_dic={} #key = source, value = 각 target에 대한 l dic 
    
    L=get_L(graph,display_length)
    
    for source in graph.graph.nodes:
        target_dic={}
        for target in graph.graph.nodes:
            if nx.has_path(graph.graph,source,target) and (source!=target):
                d=nx.shortest_path_length(graph.graph,source,target)
                target_dic[target]=L*d
            else:
                target_dic[target]=0
        l_dic[source]=target_dic
        
        
    return l_dic


def get_k(graph,K): #k = spring의 힘 , K = 상수,값의 범위는 일반적으로 양수,높은 값을 선택할수록 더 강한 스프링 강도 가짐  
    
    k_dic={}
    
    for source in graph.graph.nodes:
        target_dic={}
        for target in graph.graph.nodes:
            if nx.has_path(graph.graph,source,target) and (source!=target):
                d=nx.shortest_path_length(graph.graph,source,target)
                target_dic[target]=K/(graph.d_dic[source][target]*graph.d_dic[source][target])
            else:
                target_dic[target]=0
        k_dic[source]=target_dic
        
    return k_dic
    


def get_E_xm(graph,m_node):
    
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E_xm=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E_xm+=graph.k_dic[m_node][i_node]*(
                (xm-graph.pos[i_node][0])
                -
                graph.l_dic[m_node][i_node]*(xm-graph.pos[i_node][0])
                /
                math.sqrt((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                )
    
    return E_xm 

def get_E_ym(graph,m_node):
    
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E_ym=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E_ym+=graph.k_dic[m_node][i_node]*(
                (ym-graph.pos[i_node][1])
                -
                graph.l_dic[m_node][i_node]*(ym-graph.pos[i_node][1])
                /
                math.sqrt((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                )
    
    return E_ym 
    

def get_m_value(E_xm,E_ym):
    return math.sqrt(E_xm*E_xm+E_ym*E_ym)


def get_E2_xm2(graph,m_node):
    
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E2_xm2=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E2_xm2+=graph.k_dic[m_node][i_node]*(
                1
                -
                graph.l_dic[m_node][i_node]*(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1])
                /
                ((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_xm2 

def get_E2_xm_ym(graph,m_node):
    
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E2_xm_ym=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E2_xm_ym+=graph.k_dic[m_node][i_node]*(
                graph.l_dic[m_node][i_node]*(xm-graph.pos[i_node][0])*(ym-graph.pos[i_node][1])
                /
                ((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_xm_ym 

def get_E2_ym_xm(graph,m_node):
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E2_ym_xm=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E2_ym_xm+=graph.k_dic[m_node][i_node]*(
                graph.l_dic[m_node][i_node]*(xm-graph.pos[i_node][0])*(ym-graph.pos[i_node][1])
                /
                ((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_ym_xm 

def get_E2_ym2(graph,m_node):
    xm=graph.pos[m_node][0]
    ym=graph.pos[m_node][1]
    
    
    E2_ym2=0
    
    for i_node in graph.graph.nodes:
        if m_node!=i_node:
            E2_ym2+=graph.k_dic[m_node][i_node]*(
                1
                -
                graph.l_dic[m_node][i_node]*(xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])
                /
                ((xm-graph.pos[i_node][0])*(xm-graph.pos[i_node][0])+(ym-graph.pos[i_node][1])*(ym-graph.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_ym2 

def get_update_x(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2):
    return (E_ym*E2_xm_ym/E2_ym2-E_xm)/(E2_xm2-E2_ym_xm*E2_xm_ym/E2_ym2)

def get_update_y(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2):
    return (E_ym*E2_xm2/E2_ym_xm)/(E2_xm_ym-E2_ym2*E2_xm2/E2_ym_xm)



    
    