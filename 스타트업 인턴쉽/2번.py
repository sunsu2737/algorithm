import heapq

def solution(t, r):
    answer = []
    number=[i for i in range(len(t))]
    person=list(zip(r,t,number))
    person.sort(key=lambda x:x[1])
    heap=[]
    time=0
    i=0
    while True:
        while True:
            if i<len(t) and person[i][1]==time:
                heapq.heappush(heap,person[i])
                i+=1
            else:
                break
        if heap:
            answer.append(heapq.heappop(heap)[2])
        if i>=len(t) and not heap:
            break
        time+=1
    return answer


print(solution([0,1,3,0],[0,1,2,3]))