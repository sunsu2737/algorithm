import sys
line = sys.stdin.readline

T = int(line())
grade = 0
before = []
now = []
for i in range(T):
    sub = list(map(int, line().split()))
    if sub[0] == 0:
        pass
    else:
        if now:
            before.append(now)
        now = sub
    if now:
        now[2] -= 1
        if now[2] == 0:
            grade += now[1]
            if before:
                now = before.pop()
print(grade)

