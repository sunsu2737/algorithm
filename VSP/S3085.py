n = int(input())
candy = [list(input()) for i in range(n)]
answer = 0


def check(i, j):
    result = 0

    cnt = 0
    x = i
    y = j
    while 0 <= x < n and 0 <= y < n:
        if candy[i][j] != candy[x][y]:
            break
        cnt += 1
        x -= 1
    x = i+1
    y = j
    while 0 <= x < n and 0 <= y < n:
        if candy[i][j] != candy[x][y]:
            break
        cnt += 1
        x += 1
    if result < cnt:
        result = cnt
    cnt = 0
    x = i
    y = j
    while 0 <= x < n and 0 <= y < n:
        if candy[i][j] != candy[x][y]:
            break
        cnt += 1
        y -= 1
    x = i
    y = j+1
    while 0 <= x < n and 0 <= y < n:
        if candy[i][j] != candy[x][y]:
            break
        cnt += 1
        y += 1
    if result < cnt:
        result = cnt
    return result


for i in range(n):
    for j in range(n):
        if i+1 < n:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            result = check(i, j)
            if answer < result:
                answer = result
            result = check(i+1, j)
            if answer < result:
                answer = result
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        if j+1 < n:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            result = check(i, j)
            if answer < result:
                answer = result
            result = check(i, j+1)
            if answer < result:
                answer = result
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

print(answer)
