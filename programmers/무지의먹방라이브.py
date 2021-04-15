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