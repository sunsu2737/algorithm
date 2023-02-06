import sys

input = sys.stdin.readline

n = int(input())

bee = list(map(int, input().split()))

bee_s = []


for i in bee:
    if bee_s:
        bee_s.append(bee_s[-1]+i)
    else:
        bee_s.append(i)

answer = 0
for i in range(1, len(bee_s)-1):
    temp = bee_s[-1] - bee[0] - bee[i] + bee_s[-1] - bee_s[i]
    answer = max(answer, temp)

for i in range(1, len(bee_s)-1):
    temp = bee_s[-1] - bee[-1] - bee[i] + bee_s[i-1]
    answer = max(answer, temp)

for i in range(1, len(bee_s)-1):
    temp = bee_s[i]-bee[0] + bee_s[-1] - bee_s[i-1] - bee[-1]
    answer = max(answer, temp)

print(answer)
