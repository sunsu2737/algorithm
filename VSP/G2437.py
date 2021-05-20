n=int(input())
arr=list(map(int,input().split()))
arr.sort()

temp=0
for i in arr:
    if temp+1<i:
        break
    temp+=i
print(temp+1)