import sys
line=sys.stdin.readline

N=int(line())
f=[]
for i in range(N):
    f.append(line().rstrip())
answer=list(f[0])
for i in range(len(f[0])):
    for j in f:
        if answer[i]!=j[i]:
            answer[i]='?'
            break
print(''.join(answer))
