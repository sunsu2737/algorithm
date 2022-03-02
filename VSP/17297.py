n=int(input())

dp=[0]*41
dp[1]=5
dp[2]=13
s='Messi Gimossi'

def sol(idx,m):
    # print(idx,dp[idx-1],m)
    if idx<3:
        # print(m)
        return s[m]

    if dp[idx-1]>m:
        return sol(idx-1,m)
    elif dp[idx-1]<m:
        return sol(idx-2,m-dp[idx-1]-1)
    else:
        return ' '


for i in range(3,41):
    dp[i]=dp[i-1]+1+dp[i-2]

answer=sol(41,n-1)
if answer==' ':
    print('Messi Messi Gimossi')
else:
    print(answer)