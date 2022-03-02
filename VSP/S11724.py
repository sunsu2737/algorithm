from collections import deque

n,m = map(int,input().split())

graph=[[]for i in range(n+1)]


for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

check=[True]*(n+1)

cnt=0

def bfs(start):
    next=deque()
    next.append(start)
    while next:
        cur=next.popleft()
        for i in graph[cur]:
            if check[i]:
                check[i]=False
                next.append(i)




for i in range(1,n+1):
    if check[i]:
        check[i]=False
        bfs(i)
        cnt+=1

print(cnt)