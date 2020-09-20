import sys
line=sys.stdin.readline

N,M,R=map(int,line().split())
arr=[]

flag=0

def func1():
    global arr
    arr=arr[::-1]
def func2():
    global arr
    for i in range(len(arr)):
        arr[i]=arr[i][::-1]

def func3():
    global arr,M,N
    M,N=N,M
    arr2=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        for j in range(N):
            arr2[j][M-i-1]=arr[i][j]
    arr=arr2

def func4():
    global arr,M,N
    N,M=M,N
    arr2 = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(M):
        for j in range(N-1,-1,-1):
            arr2[N-j-1][i]=arr[i][j]
    arr=arr2
def func5():
    global arr
    arr2 = [[0 for _ in range(M)] for _ in range(N)]
    middleN=N//2
    middleM=M//2
    for i in range(0,middleN):
        for j in range(0,middleM):
            arr2[i][middleM+j]=arr[i][j]
    for i in range(0,middleN):
        for j in range(middleM,M):
            arr2[middleN+i][j]=arr[i][j]
    for i in range(middleN,N):
        for j in range(0,middleM):
            arr2[i-middleN][j]=arr[i][j]
    for i in range(middleN,N):
        for j in range(middleM,M):
            arr2[i][j-middleM]=arr[i][j]
    arr=arr2



def func6():
    global arr
    arr2 = [[0 for _ in range(M)] for _ in range(N)]
    middleN = N // 2
    middleM = M // 2
    for i in range(0, middleN):
        for j in range(0, middleM):
            arr2[middleN+i][j] = arr[i][j]
    for i in range(0, middleN):
        for j in range(middleM, M):
            arr2[i][j-middleM] = arr[i][j]
    for i in range(middleN, N):
        for j in range(0, middleM):
            arr2[i][j+middleM] = arr[i][j]
    for i in range(middleN, N):
        for j in range(middleM, M):
            arr2[i-middleN][j ] = arr[i][j]
    arr = arr2

for i in range(N):
    arr.append(line().split())
U=list(map(int,line().split()))
state=[0,0,0,0]

for A in U:
    if A==1:
        state[0]=(state[0]+1)%2
        state[2]=-state[2]
        state[3]=-state[3]
    elif A==2:
        state[1]=(state[1]+1)%2
        state[2] = -state[2]
        state[3] = -state[3]
    elif A==3:

        state[2]+=1
        if state[2]>3:
            state[2]=0

    elif A==4:

        state[2]-=1
        if state[2]<-3:
            state[2]=0

    elif A==5:

        state[3] += 1
        if state[3] > 3:
            state[3] = 0

    elif A==6:

        state[3] -= 1
        if state[3] < -3:
            state[3] = 0


if state[0]==1:
    func1()

if state[1]==1:
    func2()

if state[2]>0:
    for i in range(state[2]):
        func3()
if state[2]<0:
    for i in range(-state[2]):
        func4()
if state[3]>0:
    for i in range(state[3]):
        func5()
if state[3]<0:
    for i in range(-state[3]):
        func6()
for i in arr:
    print(*i)