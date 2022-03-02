import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
graph=[[] for i in range(n+1)]
check=[0]*(n+1)
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

answer=list(map(int,input().split()))
pr=[0]*(n+1)
for i in range(len(answer)):
    pr[answer[i]]=i
for g in graph:
    g.sort(key=lambda x:pr[x])
path=[]
def bfs():
    next=deque()
    next.append(1)
    check[1]=1
    while next:
        cur=next.popleft()
        path.append(cur)
        for i in graph[cur]:
            if check[i]==0:
                check[i]=1
                next.append(i)
bfs()
if path==answer:
    print(1)
else:
    print(0)
        