import heapq


def solution(scoville, K):

    cnt = 0
    heapq.heapify(scoville)
    while True:

        if scoville[0] >= K:
            break
        cnt += 1
        if len(scoville) <= 1:
            return -1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)

    return cnt
