import sys

input = sys.stdin.readline


def sol(k):
    k = list(map(int, str(k)))
    d = k[0] - k[1]

    for i in range(1, len(k)-1):
        if k[i] - k[i+1] != d:
            return False
    return True


n = int(input())
cnt = 0
for i in range(1, n+1):
    if len(str(i))==1 or sol(i):
        cnt += 1

print(cnt)
