import sys
line=sys.stdin.readline

N=int(line())

dp=[[0 for _ in range(301)]for _ in range(2)]
stairs=[]
for _ in range(N):
    stairs.append(int(line()))
dp[1][1]=stairs[0]
for i in range(2,N+1):
    dp[0][i]=dp[1][i-1]+stairs[i-1]
    dp[1][i]=max(dp[0][i-2],dp[1][i-2])+stairs[i-1]
print(max(dp[0][N],dp[1][N]))