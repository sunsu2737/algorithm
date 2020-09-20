import sys
from collections import deque
line = sys.stdin.readline

N = int(line())
graph = []
for _ in range(N-1):
    graph.append(tuple(map(int, line().split())))
dfs = deque(map(int, line().split()))
sfd = deque()

while dfs or sfd:
