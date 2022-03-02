import heapq
import sys
input=sys.stdin.readline
n,m,k,x=map(int,input().split())

graph=[[] for i in range(n+1)]
INF=99999999999999999
table=[INF]*(n+1)
table[x]=0


for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
answer=[]
def dijk():
    next=[]

    for i in graph[x]:
        if 1+table[x]<table[i]:
            table[i]=1+table[x]
            heapq.heappush(next,(1,i))
    while next:
        coast,a=heapq.heappop(next)
        if table[a]==k:
            answer.append(a)
        if table[a]>k:
            break
        for i in graph[a]:

            if coast+table[a]<table[i]:
                table[i]=coast+table[a]
                heapq.heappush(next,(1,i))
dijk()

answer.sort()
if answer:
    for i in answer:
        print(i)
else:
    print(-1)




