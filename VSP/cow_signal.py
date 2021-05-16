import sys
line=sys.stdin.readline

M,N,K=map(int,line().split())
arr=list()
for i in range(M):
    temp=line().rstrip()
    arr.append(temp)
    for j in range(1,K):
        arr.append(temp)

for i in arr:
    for j in i:
        print(j*K,end='')
    print()