import sys
line = sys.stdin.readline

t=int(line())

for i in range(t):
    a=list(line().split())
    for j in a:
        print(j[::-1],end=' ')
    print()
    

