import sys
line=sys.stdin.readline

N=int(line())

for i in range(N):
    a,b=line().split()
    a=int(a)
    for j in b:
        print(j*a,end='')
    print()