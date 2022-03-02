arr=list(map(int,input().split()))

a=[100,100,200,200,300,300,400,400,500]
answer='none'

if sum(arr)>=100:
    answer='draw'
for i in range(len(arr)):
    if arr[i]>a[i]:
        answer='hacker'
        break
print(answer)