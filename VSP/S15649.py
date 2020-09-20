import sys
from itertools import permutations
line = sys.stdin.readline

n, r = map(int, line().split())

for i in list(permutations(range(1, n+1), r)):
    print(*i)
