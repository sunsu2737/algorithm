import sys
line=sys.stdin.readline

N=int(line())
sum=0
for i in range(N):
    sum+=int(line())
print(sum-(N-1))