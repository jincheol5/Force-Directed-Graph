import networkx as nx 
import matplotlib.pyplot as plt
import math

def get_d(G): #d_ij = pi 와 pj의 최단거리 
    
    d_dic={}
    
    nodes=G.graph.nodes
    
    
    for source in nodes:
        shortest_distance={}
        for target in nodes:
            if source!=target:
                shortest_distance[target]=nx.shortest_path_length(G.graph,source,target)
        d_dic[source]=shortest_distance      

    return d_dic


def get_L(G,display_length):
    
    diameter=nx.diameter(G.graph)
    
    return display_length/diameter

    
def get_l(G,display_length):
    
    l_dic={} #key = source, value = 각 target에 대한 l dic 
    
    L=get_L(G,display_length)
    
    for source in G.graph.nodes:
        target_dic={}
        for target in G.graph.nodes:
            if source!=target:
                d=nx.shortest_path_length(G.graph,source,target)
                target_dic[target]=L*d
            
        l_dic[source]=target_dic
        
        
    return l_dic


def get_k(G,K): #k = spring의 힘 , K = 상수,값의 범위는 일반적으로 양수,높은 값을 선택할수록 더 강한 스프링 강도 가짐  
    
    k_dic={}
    
    for source in G.graph.nodes:
        target_dic={}
        for target in G.graph.nodes:
            if source!=target:
                d=nx.shortest_path_length(G.graph,source,target)
                target_dic[target]=K/(G.d_dic[source][target]*G.d_dic[source][target])
        k_dic[source]=target_dic
        
    return k_dic
    


def get_E_xm(G,m_node):
    
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E_xm=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E_xm+=G.k_dic[m_node][i_node]*(
                (xm-G.pos[i_node][0])
                -
                (G.l_dic[m_node][i_node]*(xm-G.pos[i_node][0]))
                /
                math.sqrt((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                )
    
    return E_xm 

def get_E_ym(G,m_node):
    
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E_ym=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E_ym+=G.k_dic[m_node][i_node]*(
                (ym-G.pos[i_node][1])
                -
                (G.l_dic[m_node][i_node]*(ym-G.pos[i_node][1]))
                /
                math.sqrt((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                )
    
    return E_ym 
    

def get_m_value(E_xm,E_ym):
    return math.sqrt(E_xm*E_xm+E_ym*E_ym)


def get_E2_xm2(G,m_node):
    
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E2_xm2=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E2_xm2+=G.k_dic[m_node][i_node]*(
                1
                -
                (G.l_dic[m_node][i_node]*(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                /
                ((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_xm2 

def get_E2_xm_ym(G,m_node):
    
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E2_xm_ym=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E2_xm_ym+=G.k_dic[m_node][i_node]*(
                (G.l_dic[m_node][i_node]*(xm-G.pos[i_node][0])*(ym-G.pos[i_node][1]))
                /
                ((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_xm_ym 

def get_E2_ym_xm(G,m_node):
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E2_ym_xm=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E2_ym_xm+=G.k_dic[m_node][i_node]*(
                G.l_dic[m_node][i_node]*(xm-G.pos[i_node][0])*(ym-G.pos[i_node][1])
                /
                ((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_ym_xm 

def get_E2_ym2(G,m_node):
    xm=G.pos[m_node][0]
    ym=G.pos[m_node][1]
    
    
    E2_ym2=0
    
    for i_node in G.graph.nodes:
        if m_node!=i_node:
            E2_ym2+=G.k_dic[m_node][i_node]*(
                1
                -
                (G.l_dic[m_node][i_node]*(xm-G.pos[i_node][0])*(xm-G.pos[i_node][0]))
                /
                ((xm-G.pos[i_node][0])*(xm-G.pos[i_node][0])+(ym-G.pos[i_node][1])*(ym-G.pos[i_node][1]))
                **(3/2)
                )
    
    return E2_ym2 

def get_update_x(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2):
    return (E_ym*E2_xm_ym/E2_ym2-E_xm)/(E2_xm2-E2_ym_xm*E2_xm_ym/E2_ym2)

def get_update_y(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2):
    return (E_ym*E2_xm2/E2_ym_xm)/(E2_xm_ym-E2_ym2*E2_xm2/E2_ym_xm)


def get_M(G):
    M={}
    for node in G.graph.nodes:
        E_xm=get_E_xm(G,node)
        E_ym=get_E_ym(G,node)
        m_value=get_m_value(E_xm,E_ym)
        M[node]=m_value
    
    return M


def update_algorithm(G,pre_pos,display_width,e):
    ##kamada kawai algorithm
    #G = class G
    #pre_pos = 초기 pos
    #display_width = 디스플레이 평면의 한 변의 길이
    #e = 종료 조건 값  

    # 1. compute d,l,k
    G.set_d(get_d(G))
    G.set_l(get_l(G,display_width))
    G.set_k(get_k(G,1))

    # 2. initialize p
    G.set_pos(pre_pos)

    ## 4. 반복 update
    #초기 setting
    G.set_M(get_M(G))

    max_M=max(G.M_dic.values())

    

    #max_M이 특정 값보다 작아질때 까지 반복 
    while(max_M>e):
        
        updated_node=None
        for key,value in G.M_dic.items():
                if value==max_M:
                    updated_node=key
                    break
        M=max_M

        #해당 노드의 초기 E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2
        E_xm=get_E_xm(G,updated_node)
        E_ym=get_E_ym(G,updated_node)
        E2_xm2=get_E2_xm2(G,updated_node)
        E2_xm_ym=get_E2_xm_ym(G,updated_node)
        E2_ym_xm=get_E2_ym_xm(G,updated_node)
        E2_ym2=get_E2_ym2(G,updated_node)
        
        print("### 현재 update 중인 node = ",updated_node,", M = ",M)
        print()
        
        #x,y값 업데이트 
        while(M>e):
            update_x=get_update_x(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2)
            update_y=get_update_y(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2)
            
            #update x,y
            G.pos[updated_node][0]+=update_x
            G.pos[updated_node][1]+=update_y

            #update E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2
            E_xm=get_E_xm(G,updated_node)
            E_ym=get_E_ym(G,updated_node)
            E2_xm2=get_E2_xm2(G,updated_node)
            E2_xm_ym=get_E2_xm_ym(G,updated_node)
            E2_ym_xm=get_E2_ym_xm(G,updated_node)
            E2_ym2=get_E2_ym2(G,updated_node)
            
            #update M
            M=get_m_value(E_xm,E_ym) 
            
        print("### update 끝난 node = ",updated_node," 의 M = ",M)
        print()
        
        #update된 G에 대한 M값과 max M값 setting 
        G.set_M(get_M(G))
        max_M=max(G.M_dic.values())
        
    return G