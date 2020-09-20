import sys
line = sys.stdin.readline

N = int(line())
N, M = map(int, line().split())
CTP = list(map(int, line().split()))

CTP.sort()
cnt = 0
B = 0
while CTP and B < N*M:
    B += CTP.pop()
    cnt += 1
if B < N*M:
    print('STRESS')
else:
    print(cnt)
