import sys
from collections import deque
"""
TODO: 플레티넘 5 최솟값 찾기
NOTE: 윈도우 슬라이딩 알고리즘
"""
line = sys.stdin.readline

N, L = map(int, line().split())

arr = list(map(int, line().split()))
min_que=deque()
for i in range(N):
    while min_que and min_que[-1]>arr[i]:
        min_que.pop()
    min_que.append(arr[i])
    if i>=L and min_que[0]==arr[i-L]:
        min_que.popleft()
    print(min_que[0],end=' ')
