import sys
line=sys.stdin.readline

N,M=map(int,line().split())

graph={i:[] for i in range(1,N+1)}
next=set()
answer=[]
for _ in range(M):
    a,b=map(int,line().split())

    graph[a].append(b)
    graph[b].append(a)
day=0
while True:
        
    for i in graph.keys():
        for j in graph[i]:
            for k in graph[j]:
                if (i,k) not in next and (k,i) not in next and k not in graph[i] and i!=k:
                    next.add((i,k))
    if next:
        pass
    else:
        break

    day+=1
    for i in next:
        a,b=i

        graph[a].append(b)
        graph[b].append(a)
    answer.append(len(next))
    next.clear()


print(day)
for i in answer:
    print(i)