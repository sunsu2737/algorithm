import sys
line = sys.stdin.readline

N = int(line())

flag = N

if N < 10:
    N *= 11
else:
    tendigit = N//10
    onedigit = N % 10

    sencondonedigit = (tendigit+onedigit) % 10

    N = onedigit*10+sencondonedigit


cnt = 1

while N != flag:

    tendigit = N//10
    onedigit = N % 10

    sencondonedigit = (tendigit+onedigit) % 10

    N = onedigit*10+sencondonedigit
    cnt += 1

print(cnt)
