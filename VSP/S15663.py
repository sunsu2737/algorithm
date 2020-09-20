import sys
line = sys.stdin.readline

N, M = map(int, line().split())
arr = list(map(int,line().split()))
check = [0 for _ in range(N)]
sub_list=[]
arr.sort()

def dfs(cnt=0):

    if cnt == M:
        print(*sub_list)
        return
    before=0
    for i in range(N):
        if check[i] == 0 and before!=arr[i]:
            check[i] = 1
            before=arr[i]
            sub_list.append(arr[i])
            dfs( cnt+1)
            check[i] = 0
            sub_list.pop()

dfs()