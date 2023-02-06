import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

line = defaultdict(list)

for _ in range(n):
    p, c = map(int,input().split())
    line[c].append(p)

answer = 0
for colors in line.values():
    colors.sort()
    if len(colors) ==  1:
        continue
    for i in range(len(colors)):
        if i==0:
            answer += colors[i+1] - colors[i]
        elif i==len(colors)-1:
            answer += colors[i] - colors[i-1]
        else:
            answer += min(colors[i]-colors[i-1],colors[i+1]-colors[i])
print(answer)
