n=int(input())
k=int(input())

fibo=[0]*41
fibo[0]=0
fibo[1]=1
fibo[2]=2
fibo_sum=[0]*41
fibo_sum[1]=1
fibo_sum[2]=3
for i in range(3,41):
    fibo[i]=fibo[i-1]+fibo[i-2]
    fibo_sum[i]=fibo_sum[i-1]+fibo[i]


dp=[0]*41
dp[1]=1
dp[2]=2
for i in range(3,41):
    dp[i]=dp[i-1]+dp[i-2]+fibo_sum[i-1]
# print(fibo[:10])
# print(fibo_sum[:10])
# print(dp[:10])
# print((dp[k]*fibo[n-k])+(dp[n-k+1]*fibo[k-1]))
# print((fibo[n-k]*fibo[k-1]))
if k==1 or k==n:
    print(dp[n])
else:
    print((dp[k]*fibo[n-k])+(dp[n-k+1]*fibo[k-1])-(fibo[n-k]*fibo[k-1]))