import sys
line=sys.stdin.readline

H,M=map(int,line().split())

M=M-45

if M<0:
    M=60+M
    H-=1
if H<0:
    H=24+H
print(H,M)

