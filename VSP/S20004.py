import sys
line = sys.stdin.readline

N=int(line())
cnt=0
for i in range(1,N+1):
    me=i
    you=1
    flag=0
    for j in range(1,i+1):
        if 30%(me+you)-j==0:
            flag=1
            break
    if flag==0:
        print(i)