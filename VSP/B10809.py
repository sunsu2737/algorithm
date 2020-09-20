import sys
line=sys.stdin.readline

string=line().strip()

alpha=[-1 for _ in range(26)]

for i in range(len(string)):
    idx=ord(string[i])-ord('a')
    if alpha[idx]==-1:
        alpha[idx]=i
print(*alpha)