import sys

input=sys.stdin.readline

def run():
    n,m=map(int,input().split())

    arr=[[1] *n for _ in range(n)]
    grow=[0]*(2*n-1)
    for _  in range(m):
        z,o,t=map(int,input().split())
        for i in range(z,o+z):
            grow[i]+=1
        for i in range(o+z,o+z+t):
            grow[i]+=2
    i=0
    for j in range(n-1,-1,-1):
        arr[j][0]+=grow[i]
        i+=1
    for j in range(1,n):
        arr[0][j]+=grow[i]
        i+=1
    for i in range(1,n):
        for j in range(1,n):
            arr[i][j]=arr[0][j]
    for i in arr:
        print(*i)


if __name__ =='__main__':
    run()