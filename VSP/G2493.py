

import sys
input=sys.stdin.readline

N=int(input())
T=list(map(int,input().split()))
answer=[-1]*N
max=0

sign=N-1
for i in range(N-1,-1,-1):
    if T[i]>=max:
        while sign>i:
            if answer[sign]==-1:
                answer[sign]=i+1
            sign-=1
        max=T[i]

    elif i+1<N and T[i]>T[i+1]:
        temp=i+1
        signtemp=i+1
        while signtemp<=sign and T[i]>=T[signtemp]:
            if answer[signtemp]==-1:
                answer[signtemp]=temp

            signtemp+=1




while sign>=0:
    if answer[sign]==-1:
        answer[sign]=0
    sign-=1
print(*answer)
