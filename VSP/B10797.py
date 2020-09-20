import sys
line=sys.stdin.readline

N=int(line())
car=list(map(int,line().split()))

print(car.count(N))