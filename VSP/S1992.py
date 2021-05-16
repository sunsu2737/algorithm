import sys
line = sys.stdin.readline

N = int(line())

picture = [list(line().strip()) for _ in range(N)]


def press(size, startx, starty, color):

    for i in range(size):
        for j in range(size):
            if picture[i+startx][j+starty] != color:
                size = size//2
                print('(', end='')
                print(press(size, startx, starty,
                            picture[startx][starty]), end='')
                print(press(size, startx, starty+size,
                            picture[startx][starty+size]), end='')
                print(press(size, startx+size, starty,
                            picture[startx+size][starty]), end='')
                print(press(size, startx+size, starty+size,
                            picture[startx+size][starty+size]), end='')
                print(')', end='')
                return ''
    return color


temp = press(N, 0, 0, picture[0][0])
if temp == '1' or temp == '0':
    print(temp)
