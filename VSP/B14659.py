import sys

line = sys.stdin.readline

N = int(line())
M = list(map(int, line().split()))
answer = 0
i = 0
while True:
    if i >= N-1:
        break
    s = 0
    for j in range(i+1, N):
        if M[i] > M[j]:
            s += 1
        else:

            if answer < s:
                answer = s
            i = j
            break
        if j==N-1:
            if answer < s:
                answer = s
            i = j
print(answer)
