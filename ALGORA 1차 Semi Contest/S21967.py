
n=int(input())
arr=list(map(int,input().split()))
answer=0
for i in range(1,9):
    temp=0
    for j in arr:
        if i<=j<=i+2:
            temp+=1
            answer=max(answer,temp)
        else:
            temp=0
print(answer)