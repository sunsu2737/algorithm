n=int(input())

arr=list(map(int,input().split()))

temp=True

for i in range(1,n):
    if temp:
        if arr[i]<arr[i-1]:
            temp=not temp
        elif arr[i]==arr[i-1]:
            print('NO')
            break
    else:
        if arr[i]>=arr[i-1]:
            print('NO')
            break
else:
    print('YES')