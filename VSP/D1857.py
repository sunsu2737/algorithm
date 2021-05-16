import sys
from collections import deque
line=sys.stdin.readline
R,C=map(int,line().split())
board=[]
board2=[[]*R]
start=[]
end=[]
for i in range(R):
    temp=list(map(int,line().split()))
    board.append(temp)

    for j in range(C):

        if board[i][j]==3:
            start=[i,j]
        elif board[i][j]==4:
            end=[i,j]


next=deque()
next.append([start[0],start[1],0])
ans=0
while next:
    x,y,cnt=next.popleft()


    if x==end[0] and y==end[1] :

        ans=cnt-1

        break


    if 0<=x-2 and x-2<R and 0<=y+1 and y+1<C and board[x-2][y+1]!=2:
        board[x - 2][y + 1] = 2
        if board[x-2][y+1]==1:
            next.append([x-2,y+1,cnt])
        else:
            next.append([x-2,y+1,cnt+1])
    if 0<=x-2 and x-2<R and 0<=y-1 and y-1<C and board[x-2][y-1]!=2:
        board[x - 2][y - 1] = 2
        if board[x-2][y-1]==1:
            next.append([x-2,y-1,cnt])
        else:
            next.append([x-2,y-1,cnt+1])
    if 0<=x+2 and x+2<R and 0<=y+1 and y+1<C and board[x+2][y+1]!=2:
        board[x + 2][y + 1] = 2
        if board[x+2][y+1]==1:
            next.append([x+2,y+1,cnt])
        else:
            next.append([x+2,y+1,cnt+1])
    if 0<=x+2 and x+2<R and 0<=y-1 and y-1<C and board[x+2][y-1]!=2:
        board[x + 2][y - 1] = 2
        if board[x+2][y-1]==1:
            next.append([x+2,y-1,cnt])
        else:
            next.append([x+2,y-1,cnt+1])
    if 0<=x+1 and x+1<R and 0<=y+2 and y+2<C and board[x+1][y+2]!=2:
        board[x + 1][y + 2] = 2
        if board[x+1][y+2]==1:
            next.append([x+1,y+2,cnt])
        else:
            next.append([x+1,y+2,cnt+1])
    if 0<=x-1 and x-1<R and 0<=y+2 and y+2<C and board[x-1][y+2]!=2:
        board[x - 1][y + 2] = 2
        if board[x-1][y+2]==1:
            next.append([x-1,y+2,cnt])
        else:
            next.append([x-1,y+2,cnt+1])
    if 0<=x+1 and x+1<R and 0<=y-2 and y-2<C and board[x+1][y-2]!=2:
        board[x + 1][y - 2] = 2
        if board[x+1][y-2]==1:
            next.append([x+1,y-2,cnt])
        else:
            next.append([x+1,y-2,cnt+1])
    if 0<=x-1 and x-1<R and 0<=y-2 and y-2<C and board[x-1][y-2]!=2:
        board[x - 1][y - 2] = 2
        if board[x-1][y-2]==1:
            next.append([x-1,y-2,cnt])
        else:
            next.append([x-1,y-2,cnt+1])
print(ans)

