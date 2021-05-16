import sys

from collections import deque
line=sys.stdin.readline

N,M=map(int,line().split())
graph=[list() for _ in range(N+1)]
visit=[0 for _ in range(N+1)]
def sol(x,cnt=0):
    Q=deque()
    Q.append(graph[x])
    visit[x]=x
    while Q:
        L=Q.pop()

        for i in L:
            if visit[i]!=x:
                cnt+=1
                visit[i]=x
                if graph[i]:
                    Q.append(graph[i])
    return cnt

for i in range(M):
    a,b=map(int,line().split())
    graph[b].append(a)
ans=[]
max=0
visit2=[]
for i in range(1,N+1):


    if graph[i]:

        a=sol(i)
        if max==a:

            ans.append(i)
        elif max<a:
            max=a
            ans=[i]
for i in ans:
    print(i,end=' ')