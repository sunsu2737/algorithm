import sys
import heapq
line=sys.stdin.readline

n,m=map(int,line().split())
cards=list(map(int,line().split()))
heapq.heapify(cards)

for i in range(m):
    temp=heapq.heappop(cards)
    temp2=heapq.heappop(cards)
    temp=temp+temp2
    temp2=temp
    heapq.heappush(cards,temp)
    heapq.heappush(cards,temp2)
print(sum(cards))
