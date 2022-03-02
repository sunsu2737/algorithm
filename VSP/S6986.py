n,k=map(int,input().split())
arr=[]
for i in range(n):
    num=float(input())
    arr.append(num)
arr.sort()
arr=arr[k:n-k]
a,b=0,0
for i in arr:
    x,y=str(i).split('.')

    a+=int(x)
    b+=int(y)

b=b/10
c=a+b


print('%.2f'%(c/len(arr)+0.0000000000001))


f=arr[0]
s=arr[-1]
for i in range(k):
    arr.append(f)
    arr.append(s)

a,b=0,0
for i in arr:   
    x,y=str(i).split('.')

    a+=int(x)
    b+=int(y)
b=b/10
c=a+b


print('%.2f'%(c/len(arr)+0.0000000000001))