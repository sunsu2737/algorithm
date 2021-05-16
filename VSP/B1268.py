import sys
line = sys.stdin.readline
N = int(line())
friend = [set() for _ in range(N)]
cl = [[[]for _ in range(10)] for _ in range(5)]
for i in range(N):
    arr = list(map(int, line().split()))
    for j in range(5):
        cl[j][arr[j]].append(i)

for i in cl:
    for j in i:
        if len(j) < 2:
            continue
        else:
            for k in j:
                for m in j:
                    if k != m:
                        friend[k].add(m)
boss = -1
max = -1
for i in range(len(friend)):
    if max < len(friend[i]):
        boss = i
        max = len(friend[i])
print(boss+1)
