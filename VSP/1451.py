import sys
line = sys.stdin.readline


n, m = map(int, line().split())

rect = [list(map(int, list(line().strip()))) for i in range(n)]
# print(rect)



answer = 0
if m >= 3:
    for i in range(1, m-1):
        for j in range(i+1, m):
            first = 0
            second = 0
            third = 0
            for k in range(n):
                first += sum(rect[k][0:i])
                second += sum(rect[k][i:j])
                third += sum(rect[k][j:m])
            # print(first,second,third)
            answer = max(first*second*third, answer)
if n >= 3:
    for i in range(1, n-1):
        for j in range(i+1, n):
            first = 0
            second = 0
            third = 0
            for k in range(0, i):
                first += sum(rect[k])
            for k in range(i, j):
                second += sum(rect[k])
            for k in range(j, n):
                third += sum(rect[k])
            answer = max(first*second*third, answer)
if n>=2 and m>=2:
    for i in range(1,n):
        for j in range(1,m):
            first = 0
            second = 0
            third = 0
            for k in range(0, i):
                first += sum(rect[k][0:j])
                second += sum(rect[k][j:m])
            for k in range(i, n):
                third += sum(rect[k])
            answer=max(first*second*third,answer)

    for i in range(1,n):
        for j in range(1,m):
            first = 0
            second = 0
            third = 0
            for k in range(0, i):
                first += sum(rect[k])
            for k in range(i, n):
                second += sum(rect[k][j:m])
                third += sum(rect[k][0:j])
            answer=max(first*second*third,answer)

    for i in range(1,n):
        for j in range(1,m):
            first = 0
            second = 0
            third = 0
            for k in range(0, i):
                first += sum(rect[k][0:j])
            for k in range(i, n):
                second += sum(rect[k][0:j])
            for k in range( n):
                third += sum(rect[k][j:m])

            answer=max(first*second*third,answer)

    for i in range(1,n):
        for j in range(1,m):
            first = 0
            second = 0
            third = 0
            for k in range(0, i):
                first += sum(rect[k][j:m])
            for k in range(i, n):
                second += sum(rect[k][j:m])
            for k in range(n):
                third += sum(rect[k][0:j])

            answer=max(first*second*third,answer)

print(answer)
