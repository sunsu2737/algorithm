from collections import deque
import sys
sys.setrecursionlimit(25000000)
input = sys.stdin.readline


tile = {0: ((1, 0), (0, 1)), 1: ((1, 0), (0, -1)), 2: ((-1, 0), (0, 1)),
        3: ((-1, 0), (0, -1)), 4: ((1, 0), (-1, 0)), 5: ((0, 1), (0, -1))}
dd = {(1, 0): (2, 3, 4), (0, 1): (1, 3, 5),
      (-1, 0): (0, 1, 4), (0, -1): (0, 2, 5)}


def dfs(x, y, c, kk):
    global answer
    # print()
    # print(x, y-1, c)
    if x == n-1 and y == n+1:

        # print(k)

        answer = min(answer, c)
        return

    for dx, dy in tile[board[x][y]]:
        next_x, next_y = x+dx, y+dy
        if 0 <= next_x < n and 1 <= next_y < n+2 and board[next_x][next_y] in dd[(dx, dy)] and check[next_x][next_y] == 0:
            check[next_x][next_y] = 1
            dfs(next_x, next_y, c+1, kk)
            check[next_x][next_y] = 0
        if kk == 1:
            if 0 <= next_x < n and 1 <= next_y < n+2 and check[next_x][next_y] == 0:
                for d in dd[(dx, dy)]:
                    if d != board[next_x][next_y]:
                        temp = board[next_x][next_y]
                        board[next_x][next_y] = d
                        check[next_x][next_y] = 1
                        dfs(next_x, next_y, c+1, 0)
                        check[next_x][next_y] = 0
                        board[next_x][next_y] = temp


n, k = map(int, input().split())

board = [[-1]+list(map(int, input().split()))+[-1] for _ in range(n)]
board[0][0] = 5
board[n-1][n+1] = 5
check = [[0] * (n+2) for _ in range(n)]
check[0][0] = 1
answer = float('inf')
if k == 0:
    dfs(0, 0, 0, k)
    if answer == float('inf'):
        print(-1)
    else:
        print(answer-1)
else:
    dfs(0,0,0,0)
    if answer-1 == n*n:
        print(-1)
    else:
        dfs(0,0,0,1)
        if answer==float('inf'):
            print(-1)
        else:
            print(answer-1)