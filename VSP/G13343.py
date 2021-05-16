import sys
import heapq
line = sys.stdin.readline


a, b = map(int, line().split())

winarry = []

x = min(a, b)
y = max(a, b)


def simul(x, y, turn, deepth):

    if y % x == 0 and turn == -1:
        heapq.heappush(winarry, (deepth, 'lose'))
        return
    elif y % x == 0 and turn == 1:
        heapq.heappush(winarry, (deepth, 'win'))
        return
    else:
        for i in range(1, y//x+1):
            simul(min(y-x*i, x), max(y-x*i, x), turn*-1, deepth+1)


simul(x, y, 1, 0)
print(winarry)
