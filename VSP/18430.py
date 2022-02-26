n, m = map(int, input().split())

wood = [list(map(int, input().split())) for i in range(n)]
check = [[0]*m for i in range(n)]
dd = [((1, 0), (0, -1)), ((1, 0), (0, 1)),
      ((-1, 0), (0, -1)), ((-1, 0), (0, 1))]
answer = 0


def back(x, y, point=0):
    # for i in check:
    #     print(*i)
    # print(point)
    global answer
    if answer < point:
        answer = point
    for i in range(x, n):
        for j in range(y, m):
            if check[i][j] == 0:

                for d in dd:
                    wing1x = i+d[0][0]
                    wing1y = j+d[0][1]
                    wing2x = i+d[1][0]
                    wing2y = j+d[1][1]

                    if 0 <= wing1x < n and 0 <= wing1y < m and 0 <= wing2x < n and 0 <= wing2y < m and check[wing1x][wing1y] == 0 and check[wing2x][wing2y] == 0:
                        check[i][j] = -1
                        check[wing1x][wing1y] = -1
                        check[wing2x][wing2y] = -1
                        back(i-1, j-1, point+wood[i][j]*2+wood[wing1x]
                             [wing1y]+wood[wing2x][wing2y])
                        check[i][j] = 0
                        check[wing1x][wing1y] = 0
                        check[wing2x][wing2y] = 0


back(0, 0)
print(answer)
