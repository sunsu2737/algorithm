import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

apple = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    apple[x-1][y-1] = 1

turn = {}
temp = {"D": 1, "L": -1}
for _ in range(int(input())):
    t, d = input().split()
    turn[int(t)] = temp[d]

snake = deque()
dd = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d_i = 0

snake.append([0, 0])

time = 0

while True:
    time += 1
    x, y = snake[-1]

    next_x, next_y = x+dd[d_i][0], y+dd[d_i][1]
    # print(next_x, next_y)
    if [next_x, next_y] in snake or not(0 <= next_x <= n-1 and 0 <= next_y <= n-1):
        break

    snake.append([next_x, next_y])

    if apple[next_x][next_y] == 0:
        snake.popleft()
    else:
        apple[next_x][next_y] = 0
    if time in turn.keys():
        d_i = (d_i + turn[time]) % 4

print(time)
