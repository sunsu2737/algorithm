n=int(input())

arr=list(map(int,input().split()))


dp=[{}for _ in range(3000)]

check_sum=[-1]*1000001


for i,v in enumerate(arr):
    check_sum[v]=i

answer=0
for i in range(len(arr)):
    for j in range(i-1,-1,-1):
        if 2*arr[j]-arr[i]>=1 and check_sum[2*arr[j]-arr[i]]!=-1:

            dp[i][arr[i]-arr[j]]=dp[j][arr[i]-arr[j]]+arr[i]
            answer=max(answer,dp[i][arr[i]-arr[j]])
        else:
            dp[i][arr[i]-arr[j]]=arr[i]+arr[j]
            # print(dp[i])
print(answer)
