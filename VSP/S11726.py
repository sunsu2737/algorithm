import sys
from collections import deque
line = sys.stdin.readline


def main():
    n=int(line())

    dp=[0]*1001
    dp[0]=1
    dp[1]=1
    dp[2]=2
    dp[3]=3

    for i,v in enumerate(dp):
        if v==0:
            dp[i]=(dp[i-1]+dp[i-2])%10007
        if i==n:
            print(dp[i])
            return



main()