class datetime:
    def __init__(self,t):
        self.year=int(t[:4])
        self.month=int(t[4:6])
        self.day=int(t[6:8])
        self.time=int(t[8:])
    

    def __lt__(self,other):
        if self.year<other.year:
            return True
        elif self.year==other.year:
            if self.month<other.month:
                return True
            elif self.month==other.month:
                if self.day<other.day:
                    return True
                elif self.day==other.day:
                    if self.time<other.time:
                        return True
                    else:
                        return False
        return False



def solution(code, day, data):
    answer=[]
    for d in data:
        p,c,t=d.split()
        pp=p.split('=')[1]
        cc=c.split('=')[1]
        tt=datetime(t.split('=')[1])
        if cc==code and t.split('=')[1][:8] == day:
            answer.append([tt,pp])
    answer.sort()
    answer2=[]
    for i in answer:
        answer2.append(int(i[1]))
    return answer2