import sys
line = sys.stdin.readline

n,m=map(int,line().split())

p=[int(line()) for _ in range(m)]

p.sort(reverse=True)

answer=[0]*m

for i,j in enumerate(p):
    answer[i]=j*(min(i+1,n))

max_p=answer.index(max(answer))
print(p[max_p],answer[max_p])
