import sys
from collections import deque
line=sys.stdin.readline

R,C=map(int,line().split())
board=[list(map(int,line().split()))for _ in range(R)]
dp=[[-1 for _ in range(500)]for _ in range(500)]

cnt=0
def dsf(x,y):
    if x==R-1 and y==C-1:
        return 1
    if dp[x][y]!=-1:
        return dp[x][y]
    dp[x][y]=0
    if 0<=x+1 and x+1<R and 0<=y and y<C and board[x+1][y]<board[x][y]:
        dp[x][y]+=dsf(x+1,y)
    
    if 0<=x and x<R and 0<=y+1 and y+1<C and board[x][y+1]<board[x][y]:
        dp[x][y]+=dsf(x,y+1)
    
    if 0<=x-1 and x-1<R and 0<=y and y<C and board[x-1][y]<board[x][y]:
        dp[x][y]+=dsf(x-1,y)
    
    if 0<=x and x<R and 0<=y-1 and y-1<C and board[x][y-1]<board[x][y]:
        dp[x][y]+=dsf(x,y-1)

    return dp[x][y]

print(dsf(0,0))