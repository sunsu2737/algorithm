from collections import deque


def find_loc(target, ice):
    for x in range(len(ice)):
        for y in range(len(ice[x])):
            if ice[x][y] == target:
                return (x, y)

    return (0, 0)


def bfs(ice, start):
    dd = ((0, 1), (1, 0), (-1, 0), (0, -1))

    next = deque()

    next.append(start+((0, 0), 0))

    while next:
        x, y, step, cnt = next.popleft()
        for i, d in enumerate(dd):
            if 0 <= d[0] < len(ice) and 0 <= d[1] < len(ice[0]):
                if step[0] == i and step[1] >= 2:
                    continue
                if ice[x+d[0]][y+d[1]] == 3:
                    continue
                elif ice[x+d[0]][y+d[1]] in (0, 1):
                    ice[x+d[0]][y+d[1]] = -1
                    if step[0] == i:
                        next.append((x+d[0], y+d[1],
                                    (step[0], step[1]+1), cnt+1))
                    else:
                        next.append((x+d[0], y+d[1], (i, 1),cnt+1))
                elif ice[x+d[0]][y+d[1]] == 2:
                    return cnt+1


def solution(ice):
    answer = 0

    start = find_loc(1, ice)

    return bfs(ice, start)


print(solution([[1, 0, 0, 2, 0, 0], [0, 0, 0, 3, 0, 0], [
      0, 0, 0, 3, 0, 0], [0, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 0]]))
