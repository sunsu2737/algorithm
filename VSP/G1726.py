import sys
from collections import deque
line=sys.stdin.readline
M,N=map(int,line().split())

board=[]
for _ in range(M):
    board.append(list(line().split()))
start=list(map(int,line().split()))
goal=list(map(int,line().split()))
for i in range(3):
    start[i]-=1
    goal[i]-=1
check=[]
d=[(0,1),(0,-1),(1,0),(-1,0)]
dtrans=[[2,3],[2,3],[1,0],[1,0]]
next=deque()
next.append((start,0))
check.append(start)
min=9999999
while next:
    state,cnt=next.popleft()
    a,b,c=state
    if [a,b,c] ==goal:
        if cnt<min:
            min=cnt
        continue
    if [a,b,dtrans[c][0]] not in check:
        check.append([a,b,dtrans[c][0]])
        next.append(([a,b,dtrans[c][0]],cnt+1))
    if [a,b,dtrans[c][1]] not in check:
        check.append([a,b,dtrans[c][1]])
        next.append(([a,b,dtrans[c][1]],cnt+1))

    if 0<=a+d[c][0] and a+d[c][0]<M and 0<=b+d[c][1] and b+d[c][1]<N and board[a+d[c][0]][b+d[c][1]] =='0' :
        a += d[c][0]
        b += d[c][1]
        if [a , b , c] not in check:
            check.append([a,b,c])
            next.append(([a,b,c],cnt+1))
        if 0<=a+d[c][0] and a+d[c][0]<M and 0<=b+d[c][1] and b+d[c][1]<N and board[a + d[c][0]][b + d[c][1]] == '0' :
            a += d[c][0]
            b += d[c][1]
            if [a, b, c] not in check:
                check.append([a, b, c])
                next.append(([a, b, c], cnt + 1))
            if 0<=a+d[c][0] and a+d[c][0]<M and 0<=b+d[c][1] and b+d[c][1]<N and board[a + d[c][0]][b + d[c][1]] == '0' :
                a += d[c][0]
                b += d[c][1]
                if [a, b, c] not in check:
                    check.append([a, b, c])
                    next.append(([a, b, c], cnt + 1))
print(min)
