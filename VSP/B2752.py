import sys
line=sys.stdin.readline

n=list(map(int,line().split()))
n.sort()
print(*n)