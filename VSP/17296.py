n=int(input())
arr=list(map(float,input().split()))

count=0
push=False
for i in arr:
    count+=int(i)
    if i*10%10==5:
        if not push:
            count+=1
    if i>0:
        push=True
print(count)