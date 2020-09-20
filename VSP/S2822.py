import sys
line = sys.stdin.readline

arr = []
for i in range(1, 9):
    arr.append((int(line()), i))
    arr.sort()
s=0
answer=[]
for i in range(3,8):
    s+=arr[i][0]
    answer.append(arr[i][1])
print(s)
print(*sorted(answer))
