import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x_lines = defaultdict(int)
y_lines = defaultdict(int)
for i in range(1, n):
    pre_a, pre_b = points[i-1][0], points[i-1][1]
    a, b = points[i][0], points[i][1]
    # print((pre_a,pre_b),(a,b))
    if pre_a == a:
        if pre_b > b:
            x_lines[pre_b] += 1
            x_lines[b] -= 1
        else:
            x_lines[pre_b] -= 1
            x_lines[b] += 1
    else:
        if pre_a > a:
            y_lines[pre_a] += 1
            y_lines[a] -= 1
        else:
            y_lines[pre_a] -= 1
            y_lines[a] += 1

if points[0][0] == points[-1][0]:
    if points[-1][1] > points[0][1]:
        x_lines[points[-1][1]] += 1
        x_lines[points[0][1]] -= 1
    else:
        x_lines[points[-1][1]] -= 1
        x_lines[points[0][1]] += 1
else:
    if points[-1][0] > points[0][0]:
        y_lines[points[-1][0]] += 1
        y_lines[points[0][0]] -= 1
    else:
        y_lines[points[-1][0]] -= 1
        y_lines[points[0][0]] += 1
# print(x_lines)
# print(y_lines)
answer = 0
temp = 0
for k, v in list(sorted(x_lines.items())):
    temp += -v
    answer = max(answer, temp)

temp = 0
for k, v in list(sorted(y_lines.items())):
    temp += -v
    answer = max(answer, temp)

print(answer)
