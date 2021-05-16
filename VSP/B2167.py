import sys
line=sys.stdin.readline

N,M=map(int,line().split())



L=[list(map(int,line().split())) for _ in range(N)]
for i in range(N):



    for j in range(M):
        if  i==0 and j==0:
            pass
        elif i==0 and j>0:

            L[i][j]+=L[i][j-1]
        elif j==0 and i>0:
            L[i][j] += L[i-1][j]

        elif j>0 and i>0:
            L[i][j]+=L[i-1][j] + L[i][j-1]-L[i-1][j-1]


T=int(line())

for _ in range(T):
    i,j,x,y=map(int,line().split())
    if i == 1 and j == 1:
        print(L[x-1][y-1])
    elif i == 1 and j > 1:
        print(L[x-1][y-1]-L[x-1][j-2])
    elif j == 1 and i > 1:
        print(L[x-1][y-1]-L[i-2][y-1])
    elif j > 0 and i > 0:
        print(L[x-1][y-1]-L[i-2][y-1]-L[x-1][j-2]+L[i-2][j-2])
