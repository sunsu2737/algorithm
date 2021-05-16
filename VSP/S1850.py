import sys
line=sys.stdin.readline

A,B=map(int,line().split())

A,B=max(A,B),min(A,B)

while B!=0:
    A,B=B,A%B
print('1'*A)
