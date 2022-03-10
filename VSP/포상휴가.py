# 분류가 추가 분류로 돼있음
# 정렬
from heapq import *
from turtle import back

def go_vac(answer, heap):
    flag=0
    while heap:
        sol = heappop(heap)
        if sol[1] not in answer:
            answer.add(sol[1])
            flag=1
            break
    if flag == 0:
        return flag
    while heap:
        if sol[0] == heap[0][0] and heap[0][1] not in answer:
            answer.add(heappop(heap)[1])
            flag=1
        elif sol[0] == heap[0][0] and heap[0][1] in answer:
            heappop(heap)
        else:
            return flag
    return flag

def solution(basis, extras):
    answer = set()
    x_heap = []
    y_heap = []

    for i,z in enumerate(basis):
        x,y = z
        heappush(x_heap,(-x,i))
        heappush(y_heap,(y,i))
    if go_vac(answer,x_heap)==0:
        return sorted(list(answer))
    if go_vac(answer,y_heap)==0:
        return sorted(list(answer))
    
    for ex in extras:
        for e in ex:
            i,x,y = map(int,e.split())
            heappush(x_heap,(-x,i))
            heappush(y_heap,(y,i))
        if go_vac(answer,x_heap)==0:
            return sorted(list(answer))
        if go_vac(answer,y_heap)==0:
            return sorted(list(answer))

    return sorted(list(answer))