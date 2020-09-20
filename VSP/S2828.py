import sys
line = sys.stdin.readline

N, M = map(int, line().split())

J = int(line())

SB = 1
EB = M
cnt = 0
for _ in range(J):
    apple = int(line())
    if SB <= apple and apple <= EB:
        continue
    else:
        if SB > apple:
            cnt += SB-apple
            EB -= SB-apple
            SB -= SB-apple
        elif EB < apple:
            cnt += apple-EB
            SB += apple-EB
            EB += apple-EB
print(cnt)
