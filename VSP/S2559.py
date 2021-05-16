N,K=map(int,input().split())
T=list(map(int,input().split()))

TS=sum(T[0:K])
max=TS
for i in range(K,N):
    TS=TS-T[i-K]+T[i]
    if TS>max:
        max=TS


print(max)