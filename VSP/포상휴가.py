# 분류가 추가 분류로 돼있음
# 정렬
# from heapq import *
# from turtle import back

# def go_vac(answer, heap):
#     flag=0
#     while heap:
#         sol = heappop(heap)
#         if sol[1] not in answer:
#             answer.add(sol[1])
#             flag=1
#             break
#     if flag == 0:
#         return flag
#     while heap:
#         if sol[0] == heap[0][0] and heap[0][1] not in answer:
#             answer.add(heappop(heap)[1])
#             flag=1
#         elif sol[0] == heap[0][0] and heap[0][1] in answer:
#             heappop(heap)
#         else:
#             return flag
#     return flag


import math


def update_tree(index_tree, idx, val, start_index):
    cur_idx = start_index+idx
    index_tree[cur_idx] = (val, idx)
    cur_idx //= 2
    while cur_idx > 0:
        # print(cur_idx)

        index_tree[cur_idx] = max(
            index_tree[cur_idx*2], index_tree[cur_idx*2+1])
        cur_idx //= 2


def vac(index_tree, answer, start_index):
    flag = True


    while index_tree[1][0] != -10000000:
        val, idx = index_tree[1]
        if idx not in answer:
            answer.add(idx)
            flag = False
            update_tree(index_tree, idx, -10000000, start_index)
            break
        else:
            update_tree(index_tree, idx, -10000000, start_index)
    if flag:
        return flag



    while index_tree[1][0] != -10000000:
        # print(index_tree)

        val2, idx2 = index_tree[1]
        if val2 == val and idx2 not in answer:
            answer.add(idx2)
            update_tree(index_tree, idx2, -10000000, start_index)
        elif val2 == val and idx2 in answer:
            update_tree(index_tree, idx2, -10000000, start_index)
        else:
            break

    return flag


def solution(basis, extras):
    deepth = math.ceil(math.log2(len(basis)))
    x_index_tree = [(0, 0) for _ in range(2**(deepth+1))]
    y_index_tree = [(-99999999999999, 0) for _ in range(2**(deepth+1))]
    start_index = 2**deepth
    basis = [0] + basis
    for i in range(1, len(basis)):
        cur_index = start_index+i-1
        x_index_tree[cur_index] = (basis[i][0], i-1)
        while cur_index//2 > 0:
            cur_index //= 2
            x_index_tree[cur_index] = max(
                x_index_tree[cur_index], (basis[i][0], i-1))
    for i in range(1, len(basis)):
        cur_index = start_index+i-1
        y_index_tree[cur_index] = (-basis[i][1], i-1)
        while cur_index//2 > 0:
            cur_index //= 2
            y_index_tree[cur_index] = max(
                y_index_tree[cur_index], (-basis[i][1], i-1))

    answer = set()


    if vac(x_index_tree, answer, start_index):
        return sorted(list(answer))

    if vac(y_index_tree, answer, start_index):
        return sorted(list(answer))

    for ex in extras:
        for e in ex:
            idx, x, y = map(int, e.split())

            update_tree(x_index_tree, idx,
                        x_index_tree[start_index+idx][0]+x, start_index)
            update_tree(y_index_tree, idx,
                        y_index_tree[start_index+idx][0]+y, start_index)
        if vac(x_index_tree, answer, start_index):
            return sorted(list(answer))

        if vac(y_index_tree, answer, start_index):
            return sorted(list(answer))

    return sorted(list(answer))


print(solution([[68, 952], [19, 928], [31, 967], [33, 989], [29, 902], [12, 939], [74, 994], [
      14, 945], [74, 902], [24, 963]], [["7 100 4", "6 5 16"], ["7 91 7", "4 56 49", "2 32 37", "6 18 46"]]))
