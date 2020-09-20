import sys
line = sys.stdin.readline


def b_search(data, target, start, end):
    middle = (start+end)//2

    if start > end:
        return middle

    if target == data[middle]:
        return middle
    elif target < data[middle]:
        return b_search(data, target, start, middle-1)
    else:
        return b_search(data, target, middle+1, end)


def b_search2(data, target, start, end):
    middle = (start+end)//2

    if start > end:
        return middle

    if target == data[middle]:
        return middle-1
    elif target < data[middle]:
        return b_search2(data, target, start, middle-1)
    else:
        return b_search2(data, target, middle+1, end)


N, Q = map(int, line().split())

hay = list(map(int, line().split()))
hay.sort()

for i in range(Q):
    a, b = map(int, line().split())
    a = b_search2(hay, a, 0, N-1)
    b = b_search(hay, b, 0, N-1)

    print(b-a)
