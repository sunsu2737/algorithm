n = input()
check = [0]*len(n)
answer = 99999999999999999999


def back(number, d=0):
    global answer
    if d == len(n):
        if answer > int(number) and int(number) > int(n):
            answer = int(number)

    for i in range(len(n)):
        if check[i] == 0:
            check[i] = 1
            back(number+n[i], d+1)
            check[i] = 0


back('')
if answer==99999999999999999999:
    answer=0
print(answer)