n = int(input())

dp = [0]*61
dp[0] = 2

for i in range(1, 61):
    dp[i] = dp[i-1]*2

s = "01101001"


def sol(idx, x, f=1):
    # print(idx,dp[idx-1], x,f)
    if idx < 3:
        if f == 1:
            return s[x]
        else:
            if s[x] == '1':
                return '0'
            else:
                return '1'

    if dp[idx-1] > x:
        return sol(idx-1, x,f)
    elif dp[idx-1] < x:
        return sol(idx, x-dp[idx-1], f=f*-1)
    else:
        return '0'


print(sol(61, n-1))
