import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    R,C=map(int,input().split())
    arr=[]
    for i in range(R):
        arr.append(list(map(int,input().split())))
    cnt=0
    for i in range(C):
        temp=0
        for j in range(R-1,-1,-1):
            if arr[j][i]==0:
                temp+=1
            else:
                cnt+=temp
    print(cnt)