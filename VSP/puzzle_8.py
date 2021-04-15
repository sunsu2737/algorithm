from collections import deque
import copy
puzzle=[list(map(int,input().split())) for i in range(3)]
answer=[[0,1,2],[3,4,5],[6,7,8]]

first_x,first_y=0,0
def to_string(pz):
    result=''
    cnt=0
    for i in pz:
        for j in i:
            result+=str(j)
            cnt+=1
            if cnt%3==0:
                result+='\n'
    result+='->\n'
    return result

dd=[(0,1),(1,0),(-1,0),(0,-1)]
check=set()
check.add(to_string(puzzle))
def find_zero(pz):
    for i in range(len(pz)):
        for j in range(len(pz[i])):
            if pz[i][j]==0:
                first_x,first_y=i,j
                break
        else:
            continue
        return (first_x,first_y)

def solve():
    next=deque()
    
    next.append([copy.deepcopy(puzzle),0,to_string(puzzle)])
    print(next)
    while next:
        # print(1)
        pz,cnt,path=next.popleft()
        # for i in pz:
        #     print(*i)
        # print()
        if pz==answer:
            print(path)
            print(cnt)
            return
        cur_x,cur_y=find_zero(pz)
        
        for d in dd:
            if 0<=cur_x+d[0]<3 and 0<=cur_y+d[1]<3:
                # print(cur_x+d[0],cur_y+d[1])
                
                pz[cur_x][cur_y],pz[cur_x+d[0]][cur_y+d[1]]=pz[cur_x+d[0]][cur_y+d[1]],pz[cur_x][cur_y]
                if to_string(pz) not in check:
                    check.add(to_string(pz))
                    next.append([copy.deepcopy(pz),cnt+1,path+to_string(pz)])
                pz[cur_x][cur_y],pz[cur_x+d[0]][cur_y+d[1]]=pz[cur_x+d[0]][cur_y+d[1]],pz[cur_x][cur_y]
                    # print(next)
    print('impossible')
solve()

        

