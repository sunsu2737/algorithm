n = int(input())
k = int(input())
arr = list(map(int, input().split()))
tl = []

time = 0
for i in arr:
    time += 1
    if len(tl) < n:
        flag = 0
        for j in range(len(tl)):
            if tl[j][2] == i:
                tl[j][0] += 1
                flag = 1
                break
        if flag == 0:
            tl.append([1,time, i])
    else:
        flag = 0
        for j in range(len(tl)):
            if tl[j][2] == i:
                tl[j][0] += 1
                flag = 1
                break
        if flag == 0:
            tl.sort(reverse=True)
            tl.pop()
            tl.append([1,time, i])
tl.sort(key=lambda x: x[2])
for i in tl:
    print(i[2], end=' ')
