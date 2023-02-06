import sys

input = sys.stdin.readline

n, l = map(int, input().split())

cnt = 0
i = 0

while cnt < n:
    i += 1
    if str(l) not in str(i):
        cnt += 1
print(i)
