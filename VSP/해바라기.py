from collections import deque




def check(wall, flowerpot, sunflower, n, k, cnt):
    q = deque()

    idx = 0

    for i in range(cnt-1, -1, -1):
        while idx < cnt and sunflower[idx] + k > wall-flowerpot[i]:
            q.append(sunflower[idx])
            idx += 1

        if not q:
            return False
        if q[0] > wall-flowerpot[i]:
            q.popleft()
        else:
            q.pop()
            n -= 1
            if n < 0:
                return False
    return True


def solution(wall, flowerpot, sunflower, n, k):
    answer = 0

    sunflower.sort(reverse=True)
    flowerpot.sort(reverse=True)

    start = 0
    end = min(len(flowerpot), len(sunflower))

    while start < end:
        mid = (start+end+1)//2
        if check(wall, flowerpot, sunflower, n, k, mid):
            start = mid
        else:
            end = mid-1
    return start


print(solution(55,	[50, 43, 35, 13, 25, 5],	[10, 1, 2, 5, 25, 35, 42],	2,	10))
