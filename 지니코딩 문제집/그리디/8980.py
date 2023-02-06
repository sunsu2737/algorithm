import sys
from collections import defaultdict
input = sys.stdin.readline

n, c = map(int, input().split())
boxs = defaultdict(list)
car = defaultdict(int)
s = 0
answer = 0

for _ in range(int(input())):
    s_town, e_town, weight = map(int, input().split())
    boxs[s_town].append([e_town, weight])


def take(idx):
    global s
    boxs[idx].sort()
    for e_t, w in boxs[idx]:
        temp = n
        while s + w > c and e_t < temp:
            sub = min(s+w-c, car[temp])
            s -= sub
            car[temp] -= sub
            temp -= 1
        
        if s < c:
            car[e_t] += min(c-s, w)
            # print("싣는다", min(c-s, w))
            s += min(c-s, w)


def off(idx):
    global answer
    global s
    s -= car[idx]
    # print("내린다", car[idx])
    answer += car[idx]
    car[idx] = 0


for i in range(1, n+1):
    off(i)
    take(i)

print(answer)
