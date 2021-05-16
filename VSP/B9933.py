import sys
line=sys.stdin.readline

N=int(line())
passwords=[]
for _ in range(N):
    passwords.append(list(line().strip()))

for i in passwords:
    if i[::-1] in passwords:
        print(len(i),i[len(i)//2])
        break