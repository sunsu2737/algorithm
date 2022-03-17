n = int(input())

n_list = list(map(int, input().split()))

dp = [[float('-inf')]*2 for i in range(n)]


answer = n_list[0]
for i in range(n):

    dp[i][0] = max(dp[i-1][0]+n_list[i], n_list[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+n_list[i])

    answer = max(answer, dp[i][0], dp[i][1])

print(answer)
