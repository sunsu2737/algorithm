import sys
line = sys.stdin.readline


N, m, M, T, R = map(int, line().split())
flag = True
cnt = 0
firstm = m
if M-m < T:
    flag = False

while N != 0 and flag:
    if M-m < T:
        cnt += 1
        m = m-R
        if firstm > m:
            m = firstm
    else:
        cnt += 1
        N -= 1
        m = m+T
if flag:
    print(cnt)
else:
    print(-1)
