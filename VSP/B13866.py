import sys
line = sys.stdin.readline

a, b, c, d = map(int, line().split())

print(abs((a+d)-(c+b)))
