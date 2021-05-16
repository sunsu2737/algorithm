class K:
    def __init__(self,number):
        self.number=number
        self.able=True
        self.time=0
        self.match=0
    def use(self,time):
        if self.able:
            self.able=False
            self.time=self.time
            self.match+=1
            return True
        else:
            return False
    def tictoc(self):
        self.time-=1
        if self.time<=0:
            self.time=0
        self.able=True
    def __lt__(self,other):
        if self.match<other.match:
            return True
        return False
    def __lte__(self,other):
        if self.match<=other.match:
            return True
        return False
    def __str__(self):
        return str(self.match)
def solution(n, customers):
    answer = 0
    ks=[]
    for i in range(1,n):
        ks.append(K(i))
    idx=0
    while idx<len(customers):
        for k in ks:
            if not k.use(int(customers[idx][:-2])):
                break
            else:
                idx+=1
        for k in ks:
            k.tictoc()
    ks.sort()
    print(ks)
    
    return answer

solution(3,["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"])