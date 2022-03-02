t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    arr2=arr[::]
    check=[0]*m
    answer=0
    while True:
        answer+=1
        for i in range(m):
            if check[i]==0 and n>0:
                check[i]=1
                n-=1
            if check[i]==1:
                arr2[i]=max(0,arr2[i]-1)
            if arr2[i]==0:
                arr2[i]=arr[i]
                check[i]=0
        if n==0 and 1 not in check:
            break
    print(answer)

        