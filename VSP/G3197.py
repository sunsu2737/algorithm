import sys
from collections import deque
input=sys.stdin.readline

R,C=map(int,input().split())
lake=[]
swan=[]
water=deque()
cnt=0
for i in range(R):
    lake.append(list(input()))
    for j in range(C):
        if lake[i][j]=='L':
            swan.append((i,j))
            lake[i][j]=-1
            water.append((i, j))
        elif lake[i][j]=='.':
            lake[i][j]=-1

            water.append((i,j))
        elif lake[i][j]=='X':
            lake[i][j]=999999


def bfs(n):
    next=deque()
    next.append((swan[0][0],swan[0][1]))
    while next:
        i,j=next.popleft()

        if 0<=i+1 and i+1<R and 0<=j and j<C and lake[i+1][j]<n:
            if i+1==swan[1][0] and j==swan[1][1]:
                print(n)
                exit(0)
            lake[i+1][j]=n
            next.append((i+1,j))
        if 0<=i and i<R and 0<=j+1 and j+1<C and lake[i][j+1]<n:
            if i==swan[1][0] and j+1==swan[1][1]:
                print(n)
                exit(0)
            lake[i][j+1]=n
            next.append((i,j+1))
        if 0<=i-1 and i-1<R and 0<=j and j<C and lake[i-1][j]<n:
            if i-1==swan[1][0] and j==swan[1][1]:
                print(n)
                exit(0)
            lake[i-1][j]=n
            next.append((i-1,j))
        if 0<=i and i<R and 0<=j-1 and j-1<C and lake[i][j-1]<n:
            if i==swan[1][0] and j-1==swan[1][1]:
                print(n)
                exit(0)
            lake[i][j-1]=n
            next.append((i,j-1))


def ice():
    global water
    next=deque()
    while water:
        i,j=water.pop()
        if 0 <= i + 1 and i + 1 < R and 0 <= j and j < C and lake[i + 1][j] ==999999:
            lake[i + 1][j] = cnt
            next.append((i + 1, j))
        if 0 <= i and i < R and 0 <= j + 1 and j + 1 < C and lake[i][j + 1] ==999999:
            lake[i][j + 1] = cnt
            next.append((i, j + 1))
        if 0 <= i - 1 and i - 1 < R and 0 <= j and j < C and lake[i - 1][j] ==999999:
            lake[i - 1][j] = cnt
            next.append((i - 1, j))
        if 0 <= i and i < R and 0 <= j - 1 and j - 1 < C and lake[i][j - 1] ==999999:
            lake[i][j - 1] = cnt
            next.append((i, j - 1))
    return next

while(True):
    bfs(cnt)
    water=ice()
    cnt+=1
