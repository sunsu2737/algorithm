import sys
input=sys.stdin.readline

k=int(input())

paper=[[0]*(2**k) for i in range(2**k)]

last_rl=False
last_ud=-False

for i in input().rstrip():
    if i=='R':
        last_rl=True
    elif i=='L':
        last_rl=False
    elif i=='D':
        last_ud=True
    elif i=='U':
        last_ud=False

n=int(input())

rl_map={0:1,1:0,2:3,3:2}
ud_map={0:2,2:0,1:3,3:1}

if last_rl:
    n=rl_map[n]
if last_ud:
    n=ud_map[n]

paper[0][0]=n

for i in range(len(paper)):
    for j in range(len(paper)):
        if i==0 and j==0:
            pass
        elif j==0:
            paper[i][j]=ud_map[paper[i-1][j]]
        else:
            paper[i][j]=rl_map[paper[i][j-1]]


for i in paper:
    print(*i)