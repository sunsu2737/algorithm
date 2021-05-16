import sys
line = sys.stdin.readline

while True:
    a, b = map(int, line().split())

    if a == 0 and b == 0:
        break

    if a > b:
        print('Yes')
    else:
        print('No')
