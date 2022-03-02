r,c=map(int,input().split())
_,_,pr,pc=map(int,input().split())
count=0
for i in range(r):
    s=input()
    for j in s:
        if j=='P':
            count+=1
if count ==pr*pc:
    print(0)
else:
    print(1)

