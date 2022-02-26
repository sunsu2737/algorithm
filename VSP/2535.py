n = int(input())


medal = [tuple(map(int, input().split())) for _ in range(n)]

medal.sort(key=lambda x: x[2], reverse=True)

check = [0] * n
cnt = 0
for i in medal:
    if cnt == 3:
        break
    if check[i[0]] < 2:
        print(i[0], i[1])
        check[i[0]] += 1
        cnt += 1
