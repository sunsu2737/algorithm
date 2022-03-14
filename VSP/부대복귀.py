# 레벨 1? 2나 3은 돼보임
# 데스티네이션은 왜 리스트?
# 정답 코드 틀림 거리 재는 걸 공통으로 해버림


# 다익스트라 버전
# from heapq import *

# def dijk(table, graph, start):
#     check = []
#     table[start] = 0
#     heappush(check,start)

#     while check:
#         cur = heappop(check)
#         for y in graph[cur]:
#             if table[cur] + 1 < table[y]:
#                 table[y] = table[cur]+1
#                 heappush(check,y)


# def solution(n, roads, sources, destination):
#     answer = []

#     graph = dict()

#     for x, y in roads:
#         if x in graph:
#             graph[x].append(y)
#         else:
#             graph[x] = [y]
#         if y in graph:
#             graph[y].append(x)
#         else:
#             graph[y] = [x]

#     INF = 2000000000
#     table = [INF] * (n + 1)
#     dijk(table,graph,destination)
#     for s in sources:
#         if table[s] != INF:
#             answer.append(table[s])
#         else:
#             answer.append(-1)
#     return answer


# 정답나오는 코드
# from collections import deque


# def bfs(table, graph, start):

#     nexts = deque([start])
#     check = set()
#     check.add(start)
#     dist = 0
#     table[start] = dist
#     while nexts:
#         cur = nexts.pop()
#         dist += 1

#         for i in graph[cur]:
#             if i not in check:
#                 check.add(i)
#                 table[i] = dist
#                 nexts.appendleft(i)


# def solution(n, roads, sources, destination):
#     answer = []

#     graph = dict()

#     for x, y in roads:
#         if x in graph:
#             graph[x].append(y)
#         else:
#             graph[x] = [y]
#         if y in graph:
#             graph[y].append(x)
#         else:
#             graph[y] = [x]

#     table = [-1] * (n+1)
#     bfs(table, graph, destination)
#     for s in sources:
#         answer.append(table[s])
#     return answer
# # bfs 버전
from collections import deque


def bfs(table, graph, start):

    nexts = deque([[start, 0]])
    check = set()
    check.add(start)

    table[start] = 0
    while nexts:
        cur, dist = nexts.pop()

        for i in graph[cur]:
            if i not in check:
                check.add(i)
                table[i] = dist+1
                nexts.appendleft([i, dist+1])


def solution(n, roads, sources, destination):
    answer = []

    graph = dict()

    for x, y in roads:
        if x in graph:
            graph[x].append(y)
        else:
            graph[x] = [y]
        if y in graph:
            graph[y].append(x)
        else:
            graph[y] = [x]

    table = [-1] * (n+1)
    bfs(table, graph, destination)
    for s in sources:
        answer.append(table[s])
    return answer


print(solution(5, [[1, 2], [1, 3], [2, 4], [3, 5]], [4, 5], 1))


# 정답 방법

# from collections import deque

# def bfs(table, start, graph):
#     table[start]=0
#     check = table[::]
#     nexts = deque([start])
#     dist = 0
#     while nexts:
#         cur = nexts.pop()

#         for i in graph[cur]:


# def solution(n, roads, sources, destination):
#     answer = []

#     graph = dict()

#     for x, y in roads:
#         if x in graph:
#             graph[x].append(y)
#         else:
#             graph[x] = [y]
#         if y in graph:
#             graph[y].append(x)
#         else:
#             graph[y] = [x]

#     for s in sources:
#         if s not in graph:
#             answer.append(-1)
#         else:
#             answer.append(bfs(graph,s,destination))
#     return answer
