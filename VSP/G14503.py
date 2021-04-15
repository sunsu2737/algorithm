r, c = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(r)]
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def simul():
    global x, y, d
    cnt = 1
    arr[x][y] = 2

    while True:
        flag = 0
        for i in range(4):

            d = (d+3) % 4
            if 0 <= x+dd[d][0] < r and 0 <= y+dd[d][1] < c and arr[x+dd[d][0]][y+dd[d][1]] == 0:
                flag = 1
                cnt += 1
                x += dd[d][0]
                y += dd[d][1]
                arr[x][y]=2
                break
        if flag == 0:
            if 0 <= x-dd[d][0] < r and 0 <= y-dd[d][1] < c and arr[x-dd[d][0]][y-dd[d][1]] != 1:
                x -= dd[d][0]
                y -= dd[d][1]
            else:
                break
    print(cnt)


simul()
