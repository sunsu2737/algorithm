import sys
line = sys.stdin.readline

n=int(line())

class K:
    num=1
    def __init__(self,power,ring):
        self.power=power
        self.ring=ring
        self.m=K.num
        K.num+=1

    def __lt__(self,other):
        return self.power+other.power*self.ring>other.power+self.power*other.ring
    
    
k=[]
for i in range(n):
    power,ring=map(int,line().split())
    ks=K(power,ring)
    k.append(ks)

k.sort()

for i in k:
    print(i.m)
