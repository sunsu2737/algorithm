import sys
import math
input = sys.stdin.readline

n = int(input())
answer = 0
# for i in range(1, n):
#     for j in range(i, n):
#         k = n-i-j
#         if k ==max(i,j,k):
#             if k < i+j:
#                 answer+=1
for i in range(math.ceil(n/3), math.ceil(n/2)):
    answer += i - math.ceil((n-i)/2) + 1

print(answer)
