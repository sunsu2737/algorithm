import sys
line = sys.stdin.readline

A, B = map(int, line().split())

if A == B:
    print(1)
else:
    print(0)
