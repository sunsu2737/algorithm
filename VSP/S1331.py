import sys
line = sys.stdin.readline
path = set()
now = ''
start=''
for _ in range(36):
    next = line().strip()
    if next in path:
        print("Invalid")
        exit()
    path.add(next)
    if now:
        dx = abs(ord(next[0])-ord(now[0]))
        dy = abs(ord(next[1])-ord(now[1]))
        if dx == 1:
            if dy != 2:
                print('Invalid')
                exit()
        elif dx == 2:
            if dy != 1:

                print('Invalid')
                exit()
        else:
            print('Invalid')
            exit()
    else:
        start=next
    now = next
dx = abs(ord(now[0])-ord(start[0]))
dy = abs(ord(start[1])-ord(now[1]))
if dx == 1:
    if dy != 2:
        print('Invalid')
        exit()
elif dx == 2:
    if dy != 1:

        print('Invalid')
        exit()
else:
    print('Invalid')
    exit()
print('Valid')
