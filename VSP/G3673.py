import sys
import heapq
line = sys.stdin.readline

t = int(line())
for i in range(t):
    cnt = 0
    d, n = map(int, line().split())
    n_list = list(map(int, line().split()))
    dp = [0]*100001
    a = 0
    for i in n_list:
        c = 0
        a += i
        dp[a % d] += 1
    for i in dp:
        cnt += i

    print(cnt)
