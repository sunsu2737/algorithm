n=int(input())

arr=[int(input()) for i in range(n)]
arr.sort()

s=sum(arr)
answer=0
for i in arr:
    answer=max(answer,i*n)
    s-=i
    n-=1
print(answer)