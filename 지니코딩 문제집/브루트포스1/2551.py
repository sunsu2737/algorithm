import sys

input = sys.stdin.readline


n = int(input())
count = [0]*10001
s = 0
for i in input().split():
    i = int(i)
    s += i
    count[i] += 1


goal = (n//2+1) if n%2 else (n//2)

cum = 0
for i in range(1,10001):
    cum += count[i]
    if cum>=goal:
        answer1=i
        break

answer2 = s//n 
if abs(answer2*n - s) > abs((answer2+1)*n-s):
    answer2 +=1
print(answer1,answer2)