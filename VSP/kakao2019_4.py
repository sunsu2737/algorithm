# NOTE:시간초과
# def solution(food_times, k):

#     index=0
#     while k!=0:

#         if food_times[index]!=0:
#             food_times[index]-=1
#             k-=1
#             index+=1
#             index=index%len(food_times)
#         else:
#             index+=1
#             index=index%len(food_times)
#     if sum(food_times)==0:
#             return -1
#     while food_times[index]==0:
#         index+=1
#         index=index%len(food_times)
#     return index+1
import heapq


def solution(food_times, k):
    food_times_heap = [(time, idx) for idx, time in enumerate(food_times,1)]
    heapq.heapify(food_times_heap)
    small_food = food_times_heap[0][0]
    pre_food = 0
    while k-((small_food-pre_food)*len(food_times_heap)) >= 0:
        k -= (small_food-pre_food)*len(food_times_heap)
        pre_food = small_food
        heapq.heappop(food_times_heap)
        if not food_times_heap:
            return -1
        small_food = food_times_heap[0][0]

    food_times_heap.sort(key=lambda x: x[1])
    k = k % len(food_times_heap)

    return food_times_heap[k][1]


print(solution([3, 1, 2], 5))
