import numpy as np

def kill_monster(maps,p,r,area,x,y):
    result=np.zeros((r,r))
    zone=maps[x:min(len(maps)-1,x+r),y:min(len(maps)-1,y+r)]
    result[:zone.shape[0],:zone.shape[1]]=zone
    bang=result*area
    bang-=p

    count=0
    print(bang)
    print()
    for i in bang:
        for j in i:
            if j<=0:
                count+=1
    return count




def solution(maps, p, r):
    answer = 0
    maps=np.array(maps)
    # kill_monster(maps,p,r,0,0)
    area=np.zeros((r,r))
    i=r//2-1
    j=i+1
    for x in range(r):
        area[x,i]=2
        area[x,j]=2
        area[x,i+1:j]=1
        if x<r//2-1:
            i-=1
            j+=1
        elif x==r//2-1:
            pass
        else:
            i+=1
            j-=1
    for i in range(len(maps)):
        for j in range(len(maps)):
            print(kill_monster(maps,p,r,area,i,j))
    return answer


print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6))