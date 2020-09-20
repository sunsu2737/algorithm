import sys
line=sys.stdin.readline

N=int(line())

for _ in range(N):
    arr=sorted(list(map(int,line().split())))
    print(arr[-3])