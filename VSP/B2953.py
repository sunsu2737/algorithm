import sys
line = sys.stdin.readline
max = 0
maxid = 0
for i in range(1, 6):
    S = sum(list(map(int, line().split())))
    if max < S:
        maxid = i
        max = S
print(maxid, max)
