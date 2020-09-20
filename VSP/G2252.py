import sys
from collections import deque
line = sys.stdin.readline

N, M = map(int, line().split())
graph = [[0] for _ in range(N+1)]
pi = [0 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, line().split())
    graph[A].append(B)
    pi[B] += 1
Q = deque()


def topol():
    while True:
        flag = 0
        for i in range(1, N+1):
            if pi[i] == 0:
                Q.append(i)
                for j in graph[i]:
                    pi[j] -= 1
                flag = 1
                pi[i]=-1
                break
        if flag == 0:
            break


topol()
while Q:
    print(Q.popleft(),end=' ')
