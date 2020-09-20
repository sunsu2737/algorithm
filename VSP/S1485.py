import sys
line=sys.stdin.readline

N=int(line())

for i in range(N):
    dot=[list(map(int,line().split())) for _ in range(4)]
    L=list()
    for i in range(3):
        for j in range(i+1,4):
            L.append((dot[i][0]-dot[j][0])*(dot[i][0]-dot[j][0])+(dot[i][1]-dot[j][1])*(dot[i][1]-dot[j][1]))
    L.sort()
    if L[0]==L[1] and L[0]==L[2] and L[0]==L[3] and L[4]==L[5]:
        print(1)
    else:
        print(0)


