import networkx as nx 


class Graph:
    
    def __init__(self,graph):
        self.graph=graph
        self.l_dic={}
        self.d_dic={}
        self.k_dic={}
        
    def set_l(self,l_dic):
        self.l_dic=l_dic
        
    def set_d(self,d_dic):
        self.d_dic=d_dic
        
    def set_k(self,k_dic):
        self.k_dic=k_dic
        
    def set_pos(self,pos):
        self.pos=pos
        
    