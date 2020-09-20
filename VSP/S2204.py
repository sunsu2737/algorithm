import sys
line=sys.stdin.readline

while True:
    N=int(line())
    if N==0:
        break
    arr=[]
    for i in range(N):
        arr.append(line().strip())
    idx=[a for a in range(N)]
    arr2=[]
    for i in range(len(arr)):
        arr2.append((arr[i].upper(),i))
    arr2.sort()

    print(arr[arr2[0][1]])