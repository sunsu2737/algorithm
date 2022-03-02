from collections import deque
n, _ = map(int,input().split())

order = list(map(int,input().split()))

d = deque([i for i in range(1,n+1)])

answer=0
for i in order:
    countr = 0
    while d[0]!=i:
        countr+=1
        d.rotate()

    answer+=min(countr,(len(d)-countr))
    d.popleft()
print(answer)

