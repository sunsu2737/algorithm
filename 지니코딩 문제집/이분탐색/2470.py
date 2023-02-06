import sys

input = sys.stdin.readline

n = int(input())

liq = list(map(int,input().split()))

liq.sort()

start = 0
end = n-1

answer = float('inf')

while start<end:
    temp = liq[start] + liq[end]
    if abs(temp)<abs(answer):
        answer=temp
        x = liq[start]
        y = liq[end]
    if temp == 0:
        x = liq[start]
        y = liq[end]
        break
    elif temp > 0:
        end-=1
    else:
        start+=1

print(x, y)
        
