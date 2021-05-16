import sys
input=sys.stdin.readline
N=int(input())


if N==1:
    print(1)
    exit(0)
dp=[0]*N
dp[0]=1
dp[1]=1
for i in range(2,N):
    dp[i]=dp[i-1]+dp[i-2]


print(dp[N-1])