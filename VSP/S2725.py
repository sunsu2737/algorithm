import sys
line = sys.stdin.readline

def gcd(a,b):
    mod=b%a
    if mod==0:
        return a
    return gcd(mod,a)


def main():
    t = int(line())
    dp = [0]*1001
    dp[1] = 3
    for i in range(2, 1001):
        dp[i]+=dp[i-1]
        cnt=0
        for j in range(1,i):
            if gcd(i,j)==1:
                cnt+=2
        dp[i]+=cnt



    for _ in range(t):
        n = int(line())

        print(dp[n])
main()