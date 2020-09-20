import sys
line=sys.stdin.readline

x1,y1,x2,y2=map(int,line().split())
x11,y11,x22,y22=map(int,line().split())

x111=x1 if x1<x11 else x11
x222=x2 if x2>x22 else x22
y111=y1 if y1<y11 else y11
y222=y2 if y2>y22 else y22

answer=abs(x111-x222) if abs(x111-x222)>abs(y111-y222) else abs(y111-y222)
print(answer*answer)
