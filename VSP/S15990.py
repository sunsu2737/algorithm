import sys
line=sys.stdin.readline
sys.setrecursionlimit(10**8)
T=int(line())
dp=[[0 for _ in range(4)] for _ in range(100001)]
def sol(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n==3:
        return 3


for i in range(T):
    n=int(line())
    a=[]
    for i in range(1,4):
        sol(a,i,n)
        a.pop()
    print(cnt)
    cnt=0

