import sys
line = sys.stdin.readline


arr = []
for _ in range(11):
    d, v = map(int, line().split())
    arr.append((d, v))
arr.sort()


time = 0
panel = 0

for i in arr:
    time += i[0]
    panel += time+i[1]*20
print(panel)
