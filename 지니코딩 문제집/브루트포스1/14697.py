import sys

input = sys.stdin.readline

a, b, c, n = map(int, input().split())


for i in range(0, n//a+1):
    for j in range(0, n//b+1):
        for k in range(0, n//c+1):
            if a*i+b*j+c*k == n:
                print(1)
                # print(i,j,k)
                break
        else:
            continue
        break
    else:
        continue
    break
else:
    print(0)

