n, m, h = map(int, input().split())

block = [list(map(int, input().split())) for i in range(n)]

dp = [[1]+[0]*h for _ in range(n+1)]

for i in range(1, n+1):
    
    for j in range(1, h+1):
        dp[i][j] = dp[i-1][j]
        for b in block[i-1]:
            if j-b>=0:
                dp[i][j] += dp[i-1][j-b]

print(dp[-1][-1])
