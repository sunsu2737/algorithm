import sys
line=sys.stdin.readline

N,M,K=map(int,line().split())

bokdo=[[0 for _ in range(M)]for _ in range(N)]
for _ in range(K):
    r,c=map(int,line().split())
    bokdo[r-1][c-1]=1
max=0
for i in range(N):
    for j in range(M):
        cnt=0
        next=[]
        if bokdo[i][j]==1:
            next.append((i,j))
            bokdo[i][j]=0
            cnt+=1
            while next:
                x,y=next.pop()

                if 0<=x+1 and x+1<N and 0<=y and y<M and bokdo[x+1][y]==1:
                    bokdo[x+1][y]=0
                    cnt+=1
                    next.append((x+1,y))
                if 0<=x and x<N and 0<=y+1 and y+1<M and bokdo[x][y+1]==1:
                    bokdo[x][y+1]=0
                    cnt+=1
                    next.append((x,y+1))
                if 0<=x-1 and x-1<N and 0<=y and y<M and bokdo[x-1][y]==1:
                    bokdo[x-1][y]=0
                    cnt+=1
                    next.append((x-1,y))
                if 0<=x and x<N and 0<=y-1 and y-1<M and bokdo[x][y-1]==1:
                    bokdo[x][y-1]=0
                    cnt+=1
                    next.append((x,y-1))
            if cnt>max:
                max=cnt
print(max)