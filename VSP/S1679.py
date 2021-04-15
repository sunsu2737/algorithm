import sys
from collections import deque
line = sys.stdin.readline


def main():
    n=int(line())
    numbers=list(map(int,line().split()))
    m=int(line())
    numbers.sort()

    dp=[0]*50001

    for i in numbers:
        if i>=0:
            dp[i]=1
    dp[0]=1
    for i in range(1,50001):
        if dp[i]==0:
            for j in numbers:
                if i-j>0 and dp[i-j]+1<=m:
                    dp[i]=dp[i-j]+1
                elif i-j<=0:
                    break
        if dp[i]==0:

            if i%2==0:
                print('holsoon win at',i)
            else:
                print('jjaksoon win at',i)
            exit()


main()