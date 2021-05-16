import sys
line=sys.stdin.readline

A,B=map(int,line().split())

print(A*(B-1)+1)