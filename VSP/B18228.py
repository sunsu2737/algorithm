import sys
line=sys.stdin.readline

N=int(line())
peng=list(map(int,line().split()))
idx=peng.index(-1)
m=min(peng[0:idx])
M=min(peng[idx+1:N])
print(m+M)