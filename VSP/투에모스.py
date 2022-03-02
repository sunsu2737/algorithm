def sol(idx, m, dp2, a=1):
    if idx < 14:
        return (m, a)
    # print(dp2[idx-1], m)
    if dp2[idx-1] > m:
        return sol(idx-1, m, dp2, a)
    elif dp2[idx-1] < m:
        return sol(idx, m-dp2[idx-1], dp2, a*-1)
    else:
        return (0, a)


def solution(n, x, y):
    answer = ''
    dp = ['0'] * 17
    dp2 = [1]*61

    for i in range(1, len(dp2)):
        dp2[i] = dp2[i-1]*2
    for i in range(1, len(dp)):
        s = ''
        for j in range(len(dp[i-1])):
            if dp[i-1][j] == '1':
                s += '0'
            else:
                s += '1'
        dp[i] = dp[i-1]+s
    string = dp[15]
    string2 = ''
    for i in string:
        if i == '1':
            string2 += '0'
        else:
            string2 += '1'
    x2, a = sol(61, x-1, dp2)
    # print(x2, a)
    # print(string2[x2:x2+11])
    # print(len(dp[-1]))
    if a == 1:
        answer = string[x2:x2+y-x+1]
    else:
        # print(string2[x2:x2+11])
        answer = string2[x2:x2+y-x+1]
    return answer


print(solution(4, 30000, 30500))
