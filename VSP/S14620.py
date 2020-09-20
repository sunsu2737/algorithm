import sys
line = sys.stdin.readline

N = int(line())

arr = []

coast_arr = [[99999 for _ in range(N)] for _ in range(N)]

check_arr = [[0 for _ in range(N)] for _ in range(N)]

answer = 9999999

for _ in range(N):
    arr.append(list(map(int, line().split())))


def coast_check(x, y):

    return arr[x][y]+arr[x+1][y]+arr[x-1][y]+arr[x][y+1]+arr[x][y-1]


for i in range(1, N-1):
    for j in range(1, N-1):
        coast_arr[i][j] = coast_check(i, j)


def check(x, y):
    global check_arr
    check_arr[x][y] += 1
    check_arr[x-1][y-1] += 1
    check_arr[x-1][y] += 1
    check_arr[x+1][y-1] += 1
    check_arr[x+1][y] += 1
    check_arr[x+1][y+1] += 1
    check_arr[x][y+1] += 1
    check_arr[x-1][y+1] += 1
    check_arr[x][y-1] += 1

    if x+2 < N:
        check_arr[x+2][y] += 1
    if y+2 < N:
        check_arr[x][y+2] += 1
    if x-2 >= 0:
        check_arr[x-2][y] += 1
    if y-2 >= 0:
        check_arr[x][y-2] += 1


def uncheck(x, y):
    check_arr[x][y] -= 1

    check_arr[x-1][y-1] -= 1
    check_arr[x-1][y] -= 1
    check_arr[x+1][y-1] -= 1
    check_arr[x+1][y] -= 1
    check_arr[x+1][y+1] -= 1
    check_arr[x][y+1] -= 1
    check_arr[x-1][y+1] -= 1
    check_arr[x][y-1] -= 1

    if x+2 < N:
        check_arr[x+2][y] -= 1
    if y+2 < N:
        check_arr[x][y+2] -= 1
    if x-2 >= 0:
        check_arr[x-2][y] -= 1
    if y-2 >= 0:
        check_arr[x][y-2] -= 1


def choice(s=0, level=0):

    if level == 3:
        global answer
        answer = min(answer, s)

        return

    for i in range(1, N-1):
        for j in range(1, N-1):
            if check_arr[i][j] == 0:
                check(i, j)
                choice(s+coast_arr[i][j], level+1)
                uncheck(i, j)


choice()

print(answer)
