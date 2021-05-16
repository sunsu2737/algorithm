import sys
line=sys.stdin.readline

N=int(line())

arr=list(map(int,line().split()))

stack=[]

answer=[]

while arr:
    temp=arr.pop()

    while stack and stack[-1]<=temp:
        stack.pop()
    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)
    stack.append(temp)
for i in range(N-1,-1,-1):
    print(answer[i],end=' ')