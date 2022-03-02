
cnt = -1
flag = 1
check = set()
check.add((1, 1))


def dfs(wall, n, m, x, y):
    global cnt
    global flag
    # print(x, y)
    if flag == 0:
        return
    dd = ((0, -1), (1, 0), (0, 1), (-1, 0))

    cnt += 1
    if x == n and y == m:
        flag = 0
        return
    # print(x, y)
    for d in dd:
        next_x, next_y = x+d[0], y+d[1]
        if 1 <= next_x <= n and 1 <= next_y <= m:
            if ((x, y) not in wall or (next_x, next_y) not in wall[(x, y)]) and (next_x, next_y) not in check:
                check.add((next_x, next_y))
                dfs(wall, n, m, next_x, next_y)
                if flag == 0:
                    return
                # print(x, y)
                cnt += 1


def solution(n, m, wall):
    answer = 0
    wall_graph = dict()

    for i in wall:
        p1 = tuple(i[:2])
        p2 = tuple(i[2:])

        if p1 in wall_graph:
            wall_graph[p1].append(p2)
        else:
            wall_graph[p1] = [p2]
        if p2 in wall_graph:
            wall_graph[p2].append(p1)
        else:
            wall_graph[p2] = [p1]

    dfs(wall_graph, n, m, 1, 1)
    return cnt


print(solution(3, 5, [[1, 1, 1, 2], [1, 3, 1, 4], [1, 2, 2, 2], [
      2, 3, 2, 4], [2, 4, 2, 5], [2, 2, 3, 2], [3, 2, 3, 3], [3, 4, 3, 5]]	))
