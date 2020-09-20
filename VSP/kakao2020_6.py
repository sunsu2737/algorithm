import itertools
from collections import deque


def solution(n, weak, dist):
    weak = deque(weak)
    dist = dist[::-1]
    dist_perm = []

    for man in range(1, len(dist)+1):
        dist_perm = itertools.permutations(dist[:man])
        for workers in dist_perm:
            for _ in range(len(weak)):
                cur_index = 0
                pre_index = 0

                for worker in workers:

                    while True:

                        gap = weak[cur_index]-weak[pre_index]
                        if gap < 0:
                            gap += n
                        if gap > worker:
                            break
                        cur_index += 1
                        if cur_index == len(weak):
                            return man
                    pre_index = cur_index
                temp = weak.popleft()
                weak.append(temp)

    return -1


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]


print(solution(n, weak, dist))
