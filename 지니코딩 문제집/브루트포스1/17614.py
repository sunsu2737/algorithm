import sys

input = sys.stdin.readline

n = int(input())
answer = 0
for i in range(1,n+1):
    for j in str(i):
        if j in '369':
            answer+=1
print(answer)