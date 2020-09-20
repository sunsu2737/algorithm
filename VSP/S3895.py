import sys
import heapq
line = sys.stdin.readline
INF = float('inf')
N, M = map(int, line().split())

visit = [0 for _ in range(N)]
coast = list(map(int, line().split()))
graph = {i: {} for i in range(1, N+1)}
for _ in range(M):
    a, b, c = map(int, line().split())

    graph[a][b] = c

    graph[b][a] = c

dist = {i: {} for i in range(1, N+1)}


def dijk(start):

    Q = []
    for i in range(1, N+1):
        if i == start:

            dist[start][i] = 0
            heapq.heappush(Q, (0, i))

        else:
            dist[start][i] = INF

    while Q:
        C, node = heapq.heappop(Q)
        visit[node-1] = start
        for next, nextcoast in graph[node].items():
            if visit[next-1] != start:
                if dist[start][next] > C+nextcoast*coast[start-1]:
                    dist[start][next] = C+nextcoast*coast[start-1]
                    heapq.heappush(Q, (C+nextcoast*coast[start-1], next))


def newdijk():
    dist2 = dict()
    Q = []
    for i in range(1, N+1):
        if i == 1:
            dist2[i] = 0
            heapq.heappush(Q, (0, i))
        else:
            dist2[i] = INF
    while Q:
        C, node = heapq.heappop(Q)
        visit[node-1] = -1
        for next, nextcoast in dist[node].items():
            if visit[next-1] != -1:
                if dist2[next] > C+nextcoast:
                    dist2[next] = C+nextcoast
                    heapq.heappush(Q, (C+nextcoast, next))
    return dist2


for i in range(1, N+1):
    dijk(i)


print(newdijk()[N])
