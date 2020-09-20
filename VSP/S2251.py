import sys
from collections import deque
line = sys.stdin.readline

a, b, c = map(int, line().split())

A = [a, 0]
B = [b, 0]
C = [c, c]

check = []
answer = set()


def move(fr, to):

    if fr[1] >= (to[0]-to[1]):

        fr[1] = fr[1]-(to[0]-to[1])
        to[1] = to[1]+(to[0]-to[1])
    else:

        to[1] = to[1]+fr[1]
        fr[1] = 0

    if (A[1], B[1], C[1]) in check:
        return
    check.append((A[1], B[1], C[1]))
    if A[1] == 0:
        answer.add(C[1])

    for frr in [A, B, C]:
        for too in [A, B, C]:
            if frr != too:
                before_fr = frr[1]
                before_to = too[1]
                move(frr, too)
                frr[1] = before_fr
                too[1] = before_to


for frr in [A, B, C]:
    for too in [A, B, C]:
        if frr != too:
            before_fr = frr[1]
            before_to = too[1]
            move(frr, too)
            frr[1] = before_fr
            too[1] = before_to
ans = list(answer)
ans.sort()
print(*ans)
