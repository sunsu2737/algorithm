import sys
line = sys.stdin.readline



dp[n]=dp[n-1]+fibo[n]*2
dp[2]=dp[1]+fibo[2]*2
4+2
dp[3]
6+4

# N = int(line())



# dp = [-1]*5001
# dp[3] = 1
# dp[5] = 1
# for i in range(6, N+1):
#     for j in range(3, i//2+1):
#         if dp[j] != -1 and dp[i-j] != -1:
#             if dp[i] != -1:
#                 if dp[i] > dp[j]+dp[i-j]:
#                     dp[i] = dp[j]+dp[i-j]
#             else:
#                 dp[i] = dp[j]+dp[i-j]
# print(dp[N])
