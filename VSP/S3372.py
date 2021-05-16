import sys
line = sys.stdin.readline

N = int(line())
board = []
dp = [[0 for _ in range(N)]for _ in range(N)]
dp[0][0] = 1
for _ in range(N):
    board.append(list(map(int, line().split())))


for i in range(N):

    for j in range(N):
        if i==N-1 and j==N-1:
            continue
        if i+board[i][j]<N:
            dp[i+board[i][j]][j] += dp[i][j]
        if j+board[i][j]<N:
            dp[i][j+board[i][j]] += dp[i][j]

print(dp[N-1][N-1])
