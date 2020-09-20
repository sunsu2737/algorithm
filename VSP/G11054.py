import sys
line = sys.stdin.readline

N = int(line())

arr = list(map(int, line().split()))
dp = [[1 for _ in range(1001)] for _ in range(1001)]
maxi = 0


for k in range(N):
    for i in range(k+1, N):
        for j in range(i-1, k-1, -1):
            if arr[i] < arr[j]:
                if dp[k][i] < 1+dp[k][j]:
                    dp[k][i] = 1+dp[k][j]
    for i in range(k-1, -1, -1):
        for j in range(i, k+1):
            if arr[i] < arr[j]:
                if dp[k][i] < 1+dp[k][j]:
                    dp[k][i] = 1+dp[k][j]
    S1 = max(dp[k][0:k+1])
    S2 = max(dp[k][k:N])

    S = S1+S2-1

    if maxi < S:
        maxi = S

# for i in range(N):
#     for j in range(N):
#         print(dp[i][j], end=' ')
#     print()
print(maxi)
