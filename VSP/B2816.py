import sys
line=sys.stdin.readline

N=int(line())
kbs1=0
kbs2=1
for i in range(N):
    channel=line().strip()
    if channel=='KBS1':
        kbs1=i
    elif channel=='KBS2':
        kbs2=i

if kbs1==1 and kbs2==0:
    print(3,end='')
    exit()
elif kbs2==0:
    print('32',end='')
    kbs2+=1
elif kbs1==0:
    print('32',end='')
    kbs1+=1
print('3'*max(kbs1,kbs2),end='')
kbs1-=1
kbs2-=1
if kbs1==0 and kbs2==1:
    exit()
    
print('2',end='')
flag=0
if kbs2>kbs1:
    flag=2
else:
    flag=1
while kbs1!=0 or kbs2!=1 :
    if flag==1:
        if kbs1==0:
            break
        print('4',end='')
        kbs1-=1
        if kbs1==kbs2:
            kbs2+=1
    if flag==2:
        if kbs2==0:
            break
        print('4',end='')
        kbs2-=1
        if kbs1==kbs2:
            kbs1+=1
if kbs1==0 and kbs2==1:
    exit()

print('1',end='')
print('3'*(max(kbs1,kbs2)-1),end='')
print('2',end='')
if flag==1:
    kbs2-=1
else:
    kbs1-=1
while kbs1!=0 or kbs2!=1 :
    if flag==2:
        if kbs1==0:
            break
        print('4',end='')
        kbs1-=1
        if kbs1==kbs2:
            kbs2+=1
    if flag==1:
        if kbs2==1:
            break
        print('4',end='')
        kbs2-=1
        if kbs1==kbs2:
            kbs1+=1