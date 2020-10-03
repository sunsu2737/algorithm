import sys
line = sys.stdin.readline

n,k=map(int,line().split())

    
bukit=[0]*1000002

for _ in range(n):
    i,j=map(int,line().split())
    bukit[j]=i
if k>1000000:
    print(sum(bukit))
    exit()
ice=0
answer=0
for i in range(k*2+1):
    if i>1000001:
        break
    ice+=bukit[i]

for i in range(k,1000000-k+1):
    ice-=bukit[i-k]
    ice+=bukit[i+k+1]
    answer=max(ice,answer)
print(answer)