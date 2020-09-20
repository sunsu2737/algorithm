import sys

input=sys.stdin.readline
prime=[1 for i in range(1000002)]
for i in range(2,len(prime)):
    if prime[i]==1:
        for j in range(i+i,len(prime),i):
            prime[j]=0

while(True):
    N=int(input())
    flag=0
    if N==0:
        break
    for i in range(3,N//2+1,2):
        if prime[i]==1 and prime[N-i]==1 and (N-i)%2==1:

            print(N,"=",i,"+",N-i)
            flag=1
            break
    if flag==0:

        print("Goldbach's conjecture is wrong.")
