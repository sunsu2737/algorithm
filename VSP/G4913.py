import sys
line = sys.stdin.readline

prime=[True]*1000001

prime[0]=False
prime[1]=False

for i in range(2,1000001):
    if prime[i]:
        for j in range(i+i,1000001,i):
            prime[j]=False

dp=[0]*1000001
dp2=[0]*1000001
dp2[2]=1
dp[2]=1
for i in range(3,1000001):
    dp[i]=dp[i-1]+prime[i]

    if prime[i]:
        if (i-1)%4==0:
            dp2[i]=dp2[i-1]+1
        else:
            dp2[i]=dp2[i-1]
    else:
        dp2[i]=dp2[i-1]


while True:
    l,u = map(int,line().split())
    if l==-1 and u==-1:
        break
    
    print(l,u,dp[max(0,u)]-dp[max(0,l-1)],dp2[max(0,u)]-dp2[max(0,l-1)])




