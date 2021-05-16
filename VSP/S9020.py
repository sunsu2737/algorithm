import sys
line=sys.stdin.readline


prime=[1 for _ in range(10001)]
prime[0]=0
prime[1]=0
for i in range(2,10001):
    if prime[i]==1:
        for j in range(i+i,10001,i):
            prime[j]=0
T=int(line())



for i in range(T):
    N=int(line())
    for i in range(N//2,1,-1):
        if prime[i]==1:
            if prime[N-i]==1:
                print(i,N-i)
                break