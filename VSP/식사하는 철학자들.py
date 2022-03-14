import heapq

# def solution(satisfy, k):
#     answer = 0
#     ret = 0
#     check = [0] * len(satisfy)
#     r = [0]* len(satisfy)
#     l = [0]* len(satisfy)

#     satis = []
#     for i in range(len(satisfy)):
#         r[i] = i+1
#         l[i] = i-1
#         heapq.heappush(satis,(-satisfy[i],i))

#     r[-1] = 0
#     l[0] = len(satisfy)-1

#     while k>0:
#         k-=1
#         while check[satis[0][1]]==1:
#             heapq.heappop(satis)
#         val,idx = heapq.heappop(satis)

#         ret += -val
#         answer = max(answer, ret)

#         satisfy[idx] = satisfy[l[idx]] + satisfy[r[idx]] - satisfy[idx]
#         heapq.heappush(satis,(-satisfy[idx],idx))
#         check[r[idx]] = 1
#         check[l[idx]] = 1
#         r[idx] = r[r[idx]]
#         l[idx] = l[l[idx]]
#         r[l[idx]] = idx
#         l[r[idx]] = idx


#     return answer

l = [0] * 100100
r = [0] * 100100
visit = [False] * 100100


def solution(satisfy, k):
    n = len(satisfy)

    pq = []

    for i in range(n):
        l[i] = i-1
        r[i] = i+1
        heapq.heappush(pq, (-satisfy[i], i))

    l[0] = n-1
    r[n-1] = 0

    ans = 0
    ret = 0

    while k:
        k -= 1
        while visit[pq[0][1]]:
            heapq.heappop(pq)

        s, idx = heapq.heappop(pq)
        print(s,idx)
        ret -= s
        ans = max(ans, ret)
        satisfy[idx] = satisfy[l[idx]] + satisfy[r[idx]] - satisfy[idx]
        heapq.heappush(pq, (-satisfy[idx], idx))
        visit[l[idx]] = visit[r[idx]] = True
        l[idx] = l[l[idx]]
        r[idx] = r[r[idx]]
        r[l[idx]] = idx
        l[r[idx]] = idx
    return ans


print(solution([10, 1, 1, 10, 1, 1, 10, 1], 4))
