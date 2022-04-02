﻿def solution(n):
    answer = 0

    n_tile = [0] * (n+1)

    n_tile[1] = 1
    n_tile[2] = 2

    for i in range(3, n+1):
        n_tile[i] = n_tile[i-1] + n_tile[i-2]

    return n_tile[n]


print(solution(11))
