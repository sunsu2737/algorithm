import sys
from collections import deque
line=sys.stdin.readline

R,C=map(int,line().split())

board=[list(line().strip())for _ in range(R)]
max=0
check=set(board[0][0])
def dfs(x,y,cnt=1):
    global max,check
    if max<cnt:
        max=cnt
    if 0<=x+1 and x+1<R and 0<=y and y<C and board[x+1][y] not in check:
        check.add(board[x+1][y])    
        dfs(x+1,y,cnt+1)
        check.remove(board[x+1][y])
    if 0<=x and x<R and 0<=y+1 and y+1<C and board[x][y+1] not in check:
        check.add(board[x][y+1])
        dfs(x,y+1,cnt+1)
        check.remove(board[x][y+1])
    if 0<=x-1 and x-1<R and 0<=y and y<C and board[x-1][y] not in check:
        check.add(board[x-1][y])
        dfs(x-1,y,cnt+1)
        check.remove(board[x-1][y])
    if 0<=x and x<R and 0<=y-1 and y-1<C and board[x][y-1] not in check:
        check.add(board[x][y-1])
        dfs(x,y-1,cnt+1)
        check.remove(board[x][y-1])

dfs(0,0)
print(max)