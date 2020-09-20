import sys
line=sys.stdin.readline

T=int(line())
for i in range(T):
    N=int(line())
    P={}
    for i in range(N):
        P[i+1]=int(line())
    start=1
    cnt=0
    while start!=N:
        try:
            cnt+=1
            temp=start
            start=P[start]
            del(P[temp])
        except:
            cnt=0
            break
    print(cnt)