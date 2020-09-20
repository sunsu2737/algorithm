import sys
line=sys.stdin.readline

N=int(line())
sum=0
tip=[]
for i in range(N):
    tip.append(int(line()))
tip.sort(reverse=True)
for i in range(N):
    if tip[i]-i>0:
        sum+=tip[i]-i

print(sum)