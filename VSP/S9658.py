import sys
line = sys.stdin.readline

N = int(line())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[3] = 1

for i in range(4, N+1):
    if dp[i-4] == 0 and dp[i-3] == 0 and dp[i-1] == 0:
        dp[i] = 1
print(dp)
if dp[N] == 1:
    print('CY')
else:
    print('SK')

    
