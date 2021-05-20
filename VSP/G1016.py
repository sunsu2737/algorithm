import math
n,m=map(int,input().split())
arr=[1]*(m-n+1)

i=2
while i**2<=m:
    temp=n//(i**2)
    if n%(i**2)!=0:
        temp+=1
    while temp*(i**2)<=m:
        arr[temp*(i**2)-n]=0
        temp+=1
    i+=1
# print(arr)
print(sum(arr))