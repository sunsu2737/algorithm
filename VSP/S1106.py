import sys

line=sys.stdin.readline
MAX=sys.maxsize
C,N=map(int,line().split())
city=[]

for i in range(N):
    city.append(list(map(int,line().split())))

dp=[MAX for _ in range(C+1)]
dp[C]=0

result=MAX
for i in range(C,-1,-1):
    for c,p in city:
        if i-p<=0:
            if result>dp[i]+c:
                result=dp[i]+c
        else:
            if dp[i-p]>dp[i]+c:

                dp[i-p]=dp[i]+c
print(result)