a=list(map(int,input().split()))
b=list(map(int,input().split()))
pa=0
pb=0
flag='d'
for i in range(len(a)):
    if a[i]>b[i]:
        pa+=3
        flag='a'
    elif a[i]<b[i]:
        pb+=3
        flag='b'
    else:
        pa+=1
        pb+=1
print(pa,pb)
if pa>pb:
    print('A')
elif pa<pb:
    print('B')
else:
    if flag=='a':
        print('A')
    elif flag=='b':
        print('B')
    else:
        print('D')