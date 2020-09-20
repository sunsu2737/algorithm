import sys
line = sys.stdin.readline

T = int(line())

for _ in range(T):
    line()
    N = int(line())
    sum = 0
    for _ in range(N):
        sum += int(line())
    if sum % N == 0:
        print('YES')
    else:
        print('NO')
