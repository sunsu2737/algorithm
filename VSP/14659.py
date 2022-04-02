n = int(input())

hanzo = list(map(int, input().split()))

han = hanzo[0]
answer = 0
cnt = 0
for i in range(1, len(hanzo)):
    if han < hanzo[i]:
        han = hanzo[i]
        answer = max(answer, cnt)
        cnt = 0
    else:
        cnt += 1
answer = max(answer, cnt)

print(answer)
