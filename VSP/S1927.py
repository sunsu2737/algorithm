import sys
import heapq
line = sys.stdin.readline

H = []
N = int(line())

for _ in range(N):
    num = int(line())
    if num == 0:
        if H:
            print(heapq.heappop(H))
        else:
            print(0)
    else:
        heapq.heappush(H, num)
