import sys
line=sys.stdin.readline

N,M=map(int,line().split())

board=[]
check=[[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    board.append(list(line().strip()))
    for j in range(M):
        if board[i][j]=='*':
            check[i][j]=1
cross=[]
for i in range(N):
    for j in range(M):
        s=1
        flag=True
        if board[i][j]=='*':
            while flag:
                if 0<=i+s and i+s<N and 0<=j and j<M and board[i+s][j]=='*':
                    pass
                else:
                    flag=False
                if 0<=i and i<N and 0<=j+s and j+s<M and board[i][j+s]=='*':
                    pass
                else:
                    flag=False
                if 0<=i-s and i-s<N and 0<=j and j<M and board[i-s][j]=='*':
                    pass
                else:
                    flag=False
                if 0<=i and i<N and 0<=j-s and j-s<M and board[i][j-s]=='*':
                    pass
                else:
                    flag=False
                if flag:
                    cross.append((i+1,j+1,s))
                    check[i+s][j] = 0
                    check[i][j+s] = 0
                    check[i-s][j] = 0
                    check[i][j-s] = 0
                    check[i][j]=0
                    s+=1
for i in check:
    if 1 in i:
        print(-1)
        exit()
print(len(cross))
for i in cross:
    print(*i)

