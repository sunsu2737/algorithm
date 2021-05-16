import sys
line=sys.stdin.readline

N=int(line())

T=list(map(int,line().split()))

T.sort()

for i in range(N,0,-1):
    if T[N-i]>=i:
        print(i)
        exit()
print(0)