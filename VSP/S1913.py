import sys

import math
input=sys.stdin.readline

N=int(input())
K=int(input())
M=N*N+1
r=0
c=-1
arr=[[0 for i in range(N)]for i in range(N)]

for i in range(N):
    c=c+1
    M-=1
    arr[c][r]=M
    if M == K:
        a = c
        b = r

k=1
a,b=0,0
while(k<=N):

    for i in range(N-k):
        r=r+1
        M-=1
        arr[c][r]=M
        if M==K:
            a=c
            b=r
    for i in range(N-k):
        c=c-1
        M-=1
        arr[c][r]=M
        if M==K:
            a=c
            b=r
    k=k+1
    for i in range(N-k):
        r=r-1
        M-=1
        arr[c][r]=M
        if M==K:
            a=c
            b=r
    for i in range(N-k):
        c=c+1
        M-=1
        arr[c][r]=M
        if M==K:
            a=c
            b=r
    k+=1
for i in arr:
    print(*i)
print(a+1,b+1)