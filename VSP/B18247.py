import sys
line=sys.stdin.readline

T=int(line())

for _ in range(T):
    N,M=map(int,line().split())
    if N<12 or M<4:
        print(-1)
        continue
    else:
        print(M*11+4)