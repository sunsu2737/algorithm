import sys
line=sys.stdin.readline

N=int(line())

arr=[int(line()) for i in range(N)]

arr.sort()
s=0
for i in range(N):
    s+=abs(arr[i]-(i+1))

print(s)