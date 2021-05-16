import sys
line = sys.stdin.readline

N = int(line())

room = [line().strip() for _ in range(N)]

row = 0
col = 0

for i in range(N):
    S = 0
    for j in range(N):
        if room[i][j] == '.':
            S += 1
        else:
            if S >= 2:
                col += 1
            S = 0
        if j == N-1 and S >= 2:
            col += 1

for i in range(N):
    S = 0
    for j in range(N):
        if room[j][i] == '.':
            S += 1
        else:
            if S >= 2:
                row += 1
            S = 0
        if j == N-1 and S >= 2:
            row += 1
print(col, row)
