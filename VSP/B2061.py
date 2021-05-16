import sys
import math
input=sys.stdin.readline
K,L=map(int,input().split())

# for i in range(2,L):
#     if K%i==0:
#         print('BAD',i)
#         exit(0)
# print('GOOD')
prime=[1 for i in range(0,L)]
for i in range(2,len(prime)):
    if prime[i]==1:
        for j in range(i+i,len(prime),i):
            prime[j]=0

for i in range(2,len(prime)):
    if prime[i]==1:
        if K%i==0:

            print('BAD',i)
            exit()
print('GOOD')
