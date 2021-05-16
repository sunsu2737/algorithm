import heapq
INF=int(1e9)

def dijkstra(graph,traph,start,distance):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start,[]))
    distance[start] = 0
    while q:    #큐가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now,ts = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for n in ts:
            get_trap=[]
            for v,i in enumerate( graph):
                j=len(i)-1
                while True:
                    if j==-1:
                        break
                    if i[j][0]==n:
                        k=i.pop()
                        
                        get_trap.append((v,k[1]))
                    j-=1
            for i in graph[n]:
                graph[i[0]].append((n,i[1]))
            graph[n]=get_trap
        for i in graph[now]:
            if traph[i[0]]==1:
                ts.append(i[0])
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0],ts))
        for n in ts:
            for v,i in enumerate( graph):
                j=len(i)-1
                while True:
                    if j==-1:
                        break
                    if i[j][0]==n:
                        k=i.pop()
                        
                        get_trap.append((v,k[1]))
                    j-=1
            for i in graph[n]:
                graph[i[0]].append((n,i[1]))
            graph[n]=get_trap

def solution(n, start, end, roads, traps):
    graph=[[] for _ in range(n+1)]
    
    traph=[0]*(n+1)
    distance = [INF] * (n + 1)
    for t in traps:
        traph[t]=1
    for r in roads:
        graph[r[0]].append((r[1],r[2]))
    dijkstra(graph,traph,start,distance)
    return distance[end]

print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))