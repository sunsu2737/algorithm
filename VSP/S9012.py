import sys
line = sys.stdin.readline

T = int(line())

for i in range(T):
    vps = list(line().strip())

    stack = []
    for i in vps:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                stack.append('N')
                break

    if stack:
        print('NO')
    else:
        print('YES')
