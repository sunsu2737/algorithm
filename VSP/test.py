dp = [0]*60001

dp[1] = 1
dp[2] = 2
a='123'
a.
for i in range(3, 60001):
    dp[i] = dp[i-1]+dp[i-2]

print(len(str(dp[60000]//30000000//3600//24//365)))
ㅁ