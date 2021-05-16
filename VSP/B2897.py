import sys
line=sys.stdin.readline

R,C=map(int,line().split())

park=[list(line().strip()) for _ in range(R)]
answer=[0,0,0,0,0]
for i in range(R-1):
    for j in range(C-1):
        if '#' in (park[i][j],park[i+1][j],park[i][j+1],park[i+1][j+1]):
            continue
        else:
            answer[(park[i][j],park[i+1][j],park[i][j+1],park[i+1][j+1]).count('X')]+=1
for i in answer:
    print(i)
