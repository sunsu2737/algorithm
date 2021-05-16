from collections import deque

def bfs(place,i,j):
    next=deque()
    next.append((i,j))
    dd=[(0,1),(1,0),(-1,0),(0,-1)]
    check=[[0]*5 for _ in range(5)]
    check[i][j]=1
    while next:
        x,y=next.popleft()
        if x!=i or y!=j:
            if place[x][y]=='X':
                continue
            if place[x][y]=='P' and abs(i-x)+abs(j-y)<=2:
                return True
            if abs(i-x)+abs(j-y)>2:
                continue
        for d in dd:
            if 0<=x+d[0]<5 and 0<=y+d[1]<5 and check[x+d[0]][y+d[1]]==0:
                check[x+d[0]][y+d[1]]=1
                next.append([x+d[0],y+d[1]])
    return False

        

def judge(place):
    for i in range(5):
        for j in range(5):
            if place[i][j]=='P':
                if bfs(place,i,j):
                    return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(judge(place))
                


        
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))