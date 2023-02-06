import sys

input = sys.stdin.readline

n = int(input())

colors = [0] * 200001
answer = [0] * n
total = 0
temps = []

for i in range(n):
    c, s = map(int, input().split())
    temps.append((s, c, i))

temps.sort()

pt = 0
for t in range(n):
    s, c, i = temps[t]
    ps, pc, pi = temps[pt]

    while ps < s:
        total += ps
        colors[pc] += ps
        pt += 1
        ps, pc, pi = temps[pt]

    answer[i] = total - colors[c]


for a in answer:
    print(a)
