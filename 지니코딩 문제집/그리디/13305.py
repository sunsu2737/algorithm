import sys

input = sys.stdin.readline

n = int(input())
load = list(map(int,input().split()))
city = list(map(int,input().split()))

answer = 0
coast = float('inf')
for i in range(len(load)):
    if city[i] < coast:
        coast = city[i]
    answer += coast * load[i]
print(answer)
