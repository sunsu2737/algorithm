import sys
line = sys.stdin.readline

n=int(line())
dist=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
mine_map=[list(line().strip()) for _ in range(n)]
answer=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if mine_map[i][j].isdigit():
            for d in dist:
                if 0<=i+d[0]<n and 0<=j+d[1]<n :
                    answer[i+d[0]][j+d[1]]+=int(mine_map[i][j])

for i in range(n):
    for j in range(n):
        if answer[i][j]>=10:
            answer[i][j]='M'
        if mine_map[i][j].isdigit():
            answer[i][j]='*'
        print(answer[i][j],end='')
    print()
        
