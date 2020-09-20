import sys
from collections import deque
line = sys.stdin.readline

T = int(line())

for _ in range(T):
    N = int(line())
    arr = []
    for _ in range(N):
        a, b = map(int, line().split())
        arr.append((a, b))
    arr.sort()
    arr = deque(arr)
    answer = []
    while arr:
        person = arr.popleft()

        flag = 1
        if answer:
            if answer[len(answer)-1][1] < person[1]:
                continue

        answer.append(person)
    print(len(answer))
