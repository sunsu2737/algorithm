import sys

input = sys.stdin.readline

# 3의 k승


def dfs(index, s):
    # print(s)
    if index == len(g):
        if s >= 0:
            answer[s] = 1
        return
    dfs(index+1, s+g[index])
    dfs(index+1, s)
    dfs(index+1, s-g[index])


n = int(input())

g = list(map(int, input().split()))
answer = [0]*(sum(g)+1)
a = 0
dfs(0, 0, )
for i in answer:
    if i == 0:
        a += 1
print(a)
# print(a)
# print(answer)
