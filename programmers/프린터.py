def solution(priorities, location):
    pr=list(enumerate(priorities))
    cnt=1
    prlist=[]
    while pr:
        for i in range(len(pr)):
            temp=list(pr.pop(0))
            for j in pr:
                if temp[1]<j[1]:
                    pr.append(temp)
                    temp=[]
                    break
            if temp!=[]:
                pr.insert(0,temp)
        pp=pr.pop(0)
        pp[1]=cnt
        if pp[0]==location:
            return pp[1]
        cnt+=1