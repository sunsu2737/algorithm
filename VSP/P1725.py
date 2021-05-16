import sys
input = sys.stdin.readline
n = int(input())
graph = [int(input())for i in range(n)]
point=0
answer=0
graph.append(0)
stack = [(0,graph[0])]
for i in range(1,len(graph)):
    point=i

    while stack and stack[-1][1]>graph[i]:
        point,top_v=stack.pop()
        answer=max(answer,top_v*(i-point))
    stack.append((point,graph[i]))
print(answer)


