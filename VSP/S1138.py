import sys
line = sys.stdin.readline

N = int(line())
answer = [-1 for _ in range(N)]
arr = list(map(int, line().split()))
for i in range(1, N+1):
    cnt = 0
    for j in range(N):
        if cnt == arr[i-1]:
            while answer[j]!=-1:
                j+=1
            answer[j] = i
            break
        if answer[j] ==-1 or answer[j]>i:
            cnt += 1
print(*answer)
