import sys
line=sys.stdin.readline

N,M=map(int,line().split())
a=list(map(int,line().split()))
b=list(map(int,line().split()))
a.extend(b)
a.sort()
print(*a)