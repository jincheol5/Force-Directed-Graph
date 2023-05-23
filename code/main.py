import networkx as nx 
import matplotlib.pyplot as plt
import kamada_kawai as kk
from graph import Graph



#빈 figure 생성
fig = plt.figure()

display_size=fig.get_size_inches()
#display_width=display_size[0]
display_width=0.01


#create graph 
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




#set graph to Graph class 
G=Graph(graph)


##kamada kawai algorithm

# 1. compute d,l,k
G.set_d(kk.get_d(G))
G.set_l(kk.get_l(G,display_width))
G.set_k(kk.get_k(G,1))

# 2. initialize p
G.set_pos(pos)



# 3. iteration
for count in range(10): 
    # 3-1. find max m node
    max=0
    max_node=None

    for node in G.graph.nodes:
        E_xm=kk.get_E_xm(G,node)
        E_ym=kk.get_E_ym(G,node)
        m_value=kk.get_m_value(E_xm,E_ym)
        
        #print(count,"번째 ",node," 의 m_value = ",m_value)
        
        if m_value>max:
            
            #print("이전 max = ",max,"이전 max node = ",max_node.__str__()," // 바뀔 node = ",node.__str__())
            
            max_node=node
            max=m_value
    
    #print("###",count," 번째 max node = ",max_node.__str__())
    
    # 3-2. x,y값 업데이트 
    for inner_count in range(10):
        #E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2
        E_xm=kk.get_E_xm(G,max_node)
        E_ym=kk.get_E_ym(G,max_node)
        E2_xm2=kk.get_E2_xm2(G,max_node)
        E2_xm_ym=kk.get_E2_xm_ym(G,max_node)
        E2_ym_xm=kk.get_E2_ym_xm(G,max_node)
        E2_ym2=kk.get_E2_ym2(G,max_node)
        
        update_x=kk.get_update_x(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2)
        update_y=kk.get_update_y(E_xm,E_ym,E2_xm2,E2_xm_ym,E2_ym_xm,E2_ym2)
        
        G.pos[max_node][0]+=G.pos[max_node][0]+update_x
        G.pos[max_node][1]+=G.pos[max_node][1]+update_y

        #print(update_x,update_y)
    
    
nx.draw(G.graph,G.pos,with_labels=True)

plt.show()



