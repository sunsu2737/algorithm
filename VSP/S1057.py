import sys
line=sys.stdin.readline

N,a,b=map(int,line().split())
cnt=1
while(True):
    

    if abs(a-b)==1:
        if a<b:
            if a%2==1:
                print(cnt)
                exit()
        else:
            if b%2==1:
                print(cnt)
                exit()
    if a%2==1:
        a=(a+1)//2
    else:
        a=a//2
    if b%2==1:
        b=(b+1)//2
    else:
        b=b//2
    cnt+=1
