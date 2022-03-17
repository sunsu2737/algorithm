n, k = map(int, input().split())

dp = [[1] * 201 for _ in range(201)]


for i in range(2, k+1):
    for j in range(1, n+1):
        for l in range(1, j+1):
            dp[i][j] += dp[i-1][l]

print(dp[k][n] % 1000000000)


