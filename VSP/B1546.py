import sys
line=sys.stdin.readline

N=int(line())
grade=list(map(int,line().split()))
M=max(grade)
print(sum(grade)/(M*N)*100)