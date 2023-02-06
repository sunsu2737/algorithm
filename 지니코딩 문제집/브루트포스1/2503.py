import sys
import copy
input = sys.stdin.readline

t = int(input())

pool = [str(i) for i in range(100, 1000) if str(i)[0] != str(i)[1]
        and str(i)[0] != str(i)[2] and str(i)[2] != str(i)[1] and '0' not in str(i)]

for _ in range(t):
    temp = []
    n, s, b = map(int, input().split())
    n = str(n)
    x, y, z = n
    for p in pool:
        q, w, e = p
        ts, tb = 0, 0
        if q == x:
            ts += 1
        elif x in p:
            tb += 1

        if w == y:
            ts += 1
        elif y in p:
            tb += 1

        if e == z:
            ts += 1
        elif z in p:
            tb += 1

        if s == ts and b == tb:
            temp.append(p)
    pool = copy.deepcopy(temp)
    temp = []
print(len(pool))
