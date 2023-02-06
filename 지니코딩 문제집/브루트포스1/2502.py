import sys
from math import ceil
input = sys.stdin.readline

d, n = map(int,input().split())


for i in range(1,100001):
    for j in range(i,100001):
        dp = [0]* 31
        dp[1] = i
        dp[2] = j
        for k in range(3,d+1):
            dp[k] = dp[k-1] + dp[k-2]
        
        if dp[k] == n:
            print(dp[1])
            print(dp[2])
            break
    else:
        continue
    break
