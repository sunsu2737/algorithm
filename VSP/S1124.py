import sys
line=sys.stdin.readline

N,M=map(int,line().split())

prime_table=[1 for i in range(100001)]
prime_table[0]=0
prime_table[1]=0
for i in range(2,100001):
    if prime_table[i]==1:
        for j in range(i+i,100001,i):
            if prime_table[j]==1:
                prime_table[j]=0
underprime=0
for i in range(N,M+1):
    prime=0
    num=i
    j=2
    while j*j<=num:
        if num%j==0:
            num=num//j
            prime+=1
        else:
            j+=1
    if num>1:
        prime+=1
    if prime_table[prime]==1:
        underprime+=1
print(underprime)
