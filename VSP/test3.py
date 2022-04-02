import sys
sys.setrecursionlimit(10**6)

NODE = 100001
discovered = [-1 for _ in range(NODE)]
finished = [False for _ in range(NODE)]
al = [[] for _ in range(NODE)]
s = []
scc = []
cnt = 0
n = 0
num = 0
scc_num = [0 for _ in range(NODE)]
indg = [0 for _ in range(NODE)]

def dfs(cur):
    global cnt
    cnt += 1
    parent = discovered[cur] = cnt
    s.append(cur)
    
    for i in al[cur]:
        if discovered[i] == -1:
            parent = min([parent, dfs(i)])
        elif finished[i] is False:
            parent = min([parent, discovered[i]])

    if parent == discovered[cur]:
        global num
        num += 1
        group = []
        while True:
            t = s.pop()
            scc_num[t] = num
            group.append(t)
            finished[t] = True
            if t == cur:
                break
        scc.append(group)
    
    return parent

def scc_tour(cur):
    discovered[cur] = 1
    
    for i in al[cur]:
        if scc_num[i] != scc_num[cur]:
            indg[scc_num[i]] += 1
        if discovered[i] != -1:
            continue
        scc_tour(i)

def solution(reply):
    n = len(reply)
    for i in range(1, n):
        for j in reply[i]:
            al[j].append(i)

    for i in range(1, n):
        if discovered[i] == -1:
            dfs(i)

    for i in range(NODE):
        discovered[i] = -1

    for i in range(1, NODE):
        if discovered[i] == -1:
            scc_tour(i)
    
    answer = 0
    for i in range(1, num + 1):
        if indg[i] == 0:
            answer += 1
    return answer

