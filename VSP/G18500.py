import sys

from collections import deque
line=sys.stdin.readline
R,C=map(int,line().split())
cave=[]
for i in range(R):
    cave.append(list(line().rstrip()))
N=int(line())
stick=list(map(int,line().split()))


def blob(x,y,arr):
    global cave
    arr.append([x,y])
    Q=deque()
    Q.append([x,y])
    cave[x][y]='.'
    while Q:
        xy=Q.pop()
        x1=xy[0]
        y1=xy[1]
        if x1==R-1:
            while arr:
                ab=arr.pop()
                a=ab[0]
                b=ab[1]
                cave[a][b]='x'
            return
        if 0<=x1+1 and x1+1<R and 0<=y1 and y1<C and cave[x1+1][y1]=='x':
            cave[x1+1][y1]='.'
            arr.append([x1+1,y1])
            Q.append([x1+1,y1])
        if 0<=x1 and x1<R and 0<=y1+1 and y1+1<C and cave[x1][y1+1]=='x':
            cave[x1][y1+1]='.'
            arr.append([x1,y1+1])
            Q.append([x1,y1+1])
        if 0<=x1-1 and x1-1<R and 0<=y1 and y1<C and cave[x1-1][y1]=='x':
            cave[x1-1][y1]='.'
            arr.append([x1-1,y1])
            Q.append([x1-1,y1])
        if 0<=x1 and x1<R and 0<=y1-1 and y1-1<C and cave[x1][y1-1]=='x':
            cave[x1][y1-1]='.'
            arr.append([x1,y1-1])
            Q.append([x1,y1-1])


def get_high(arr):
    global cave
    min=999999
    for i in arr:
        a=i[0]
        b=i[1]

        cnt=0
        for j in range(a+2,R+1):
            cnt+=1
            if j==R:
                if min>cnt:
                    min=cnt
                break
            if cave[j][b]=='x' :
                if min>cnt:
                    min=cnt
                break
    return min

def drop(arr):
    global cave
    high=get_high(arr)

    while arr:
        ab=arr.pop()
        a=ab[0]
        b=ab[1]
        cave[a+high][b]='x'




def attack(x,d):
    global cave
    b1=[]

    if d==0:
        for i in range(C):
            if cave[x][i]=='x':
                cave[x][i]='.'
                if 0<=x-1 and cave[x-1][i]=='x':
                    blob(x-1,i,b1)
                if len(b1)==0 and i+1<C and cave[x][i+1]=='x':
                    blob(x,i+1,b1)
                if len(b1)==0 and x+1<R and cave[x+1][i]=='x':
                    blob(x+1,i,b1)
                break
    if d==1:
        for i in range(C-1,-1,-1):
            if cave[x][i]=='x':
                cave[x][i]='.'
                if 0 <= x - 1 and cave[x-1][i]=='x':
                    blob(x - 1, i, b1)
                if len(b1)==0 and 0<=i - 1 and cave[x][i-1]=='x':
                    blob(x, i - 1, b1)
                if len(b1)==0 and x+1<R and cave[x+1][i]=='x':
                    blob(x+1,i,b1)
                break
    if b1:
        drop(b1)


for i in range(len(stick)):
    attack(R-stick[i],i%2)

for j in cave:
    for k in j:
        print(k,end='')
    print()