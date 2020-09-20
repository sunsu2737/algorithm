import sys
line=sys.stdin.readline

N=int(line())

arr=list(map(int,line().split()))

cnt=[0 for i in range(100001)]

for i in arr:
    cnt[i]+=1

for i in range(100000,0,-1):

    if i==cnt[i]:
        print(cnt[i])
        exit()
if cnt[0]>0:
    print(-1)
    exit()
print(0)