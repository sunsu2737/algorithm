import sys
import math
line = sys.stdin.readline

A, B, C = map(int, line().split())

print(max(math.floor(A*B/C), math.floor(A/B*C)))
