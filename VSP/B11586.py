import sys
line = sys.stdin.readline

N = int(line())

mirror = [line().strip() for _ in range(N)]

K = int(line())

if K == 1:
    pass
elif K == 2:
    for i in range(N):
        mirror[i] = mirror[i][::-1]
elif K == 3:
    mirror = mirror[::-1]
for i in mirror:
    print(i[:])
