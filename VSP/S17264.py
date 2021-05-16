import sys
line=sys.stdin.readline

N,P=map(int,line().split())
W,L,G=map(int,line().split())
rank=0
user={}
for _ in range(P):
    name,win=line().split()
    user[name]=win
for _ in range(N):
    name=line().strip()
    if name in user.keys() and user[name]=='W':
        rank+=W
        if rank>=G:
            print('I AM NOT IRONMAN!!')
            exit()
    else:
        rank-=L
        if rank<0:
            rank=0


print('I AM IRONMAN!!')