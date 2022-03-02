import sys
input=sys.stdin.readline

def sol():
    # t=int(input())

    # for _ in range(t):
    #     n=int(input())
    #     arr=list(map(int,input().split()))
    #     answer=-999999999
    #     for i in range(1,n+1):
    #         win=sum(arr[:i])
    #         for j in range(i,n):
    #             answer=max(answer,win)
    #             win-=arr[j-i]
    #             win+=arr[j]
    #         answer=max(answer,win)
    #     print(answer)
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        answer=0
        for i in range(1,n):
            if arr[i]>0:
                arr[i]+=arr[i-1]
                answer=arr[i]
        print(arr)
        # answer=arr[0]
        # for i in range(1,n):
        #     arr[i]+=arr[i-1]
        #     answer=max(answer,arr[i])
        #     for j in range(i-1,-1,-1):
        #         answer=max(answer,arr[i]-arr[j])
        # print(arr)
        # print(answer)
sol()
