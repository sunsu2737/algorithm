import sys
line=sys.stdin.readline

N=int(line())
s=0
for i in range(1,N+1):
    s+=i
print(s)