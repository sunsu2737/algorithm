def solution(d, budget):
    
    d.sort()
    d.reverse()
    stack=sum(d)
    cnt=len(d)
    for i in d:
        if stack<=budget:
            return cnt
        cnt-=1
        stack-=i
    return 0