class Node:
    def __init__(self,data,sum,par,chi,num):
        self.data=data
        self.sum=sum
        self.par=par
        self.chi=chi
        self.num=num

class Tree:
    def __init__(self):
        self.root=None
    
    def init_Tree(self,value,edge):
        self.root=Node(value[0],value[0],None,[],1)
        for i,e in enumerate(edge):
            for n in e:
                

            




def solution(values, edges, queries):
    answer = []
    return answer

