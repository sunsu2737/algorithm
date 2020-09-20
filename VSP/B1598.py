import sys

line=sys.stdin.readline

N,M=map(int,line().split())

Nxy=[0,0]
Mxy=[0,0]
Nxy[0]=(N-1)%4
Mxy[0]=(M-1)%4
Nxy[1]=(N-1-Nxy[0])//4
Mxy[1]=(M-1-Mxy[0])//4
print(abs(Mxy[0]-Nxy[0])+abs(Mxy[1]-Nxy[1]))

