import sys
from collections import deque
import copy
input=sys.stdin.readline

T=int(input())

for i in range(T):
    prime=[1 for i in range(10000)]
    for i in range(2,len(prime)):
        if prime[i]==1:
            for j in range(i+i,len(prime),i):
                prime[j]=0
    cnt=0
    N,M=map(int,input().split())
    next= deque()
    now=deque()
    now.append(N)
    while now:
        while now:
            next.append(now.pop())
        while next:
            next_N=next.pop()
            if next_N==M:
                print(cnt)
                break
            next_N=list(str(next_N))
            for i in range(4):
                for j in range(10):
                    if i==0 and j==0:
                        continue
                    if next_N[i]==str(j):
                        continue
                    temp=next_N[i]
                    next_N[i]=str(j)

                    nextnumber=int(''.join(next_N))
                    if prime[nextnumber]==1:
                        prime[nextnumber]=0
                        now.append(int(''.join(next_N)))
                    next_N[i]=temp
        cnt+=1

