#해결

from collections import deque
check = [0 for _ in range(100010)]
check[1] = 1
def bfs(graph, c):
    global check
    check[c] = 1
    cost = 0
    nexts = deque([c])
    while nexts:
        cur = nexts.popleft()
        for i in graph[cur]:
            if check[i[0]] == 0:
                # print(cur, i[0], i[1])
                cost += i[1]
                check[i[0]] = 1
                nexts.append(i[0])
    return cost
def solution(bridge):
    answer = 0
    graph = dict()
    for x, y, c in bridge:
        if x in graph:
            graph[x].append((y, c))
        else:
            graph[x] = [(y, c)]
        if y in graph:
            graph[y].append((x, c))
        else:
            graph[y] = [(x, c)]
    all_cost = 0
    # print(all_cost)
    for i in graph[1]:
        cur_cost = bfs(graph, i[0])+i[1]
        all_cost+= cur_cost
        answer = max(answer, cur_cost)
        # print(answer)
        # print(answer)
        # print()
    return (all_cost-answer)*2