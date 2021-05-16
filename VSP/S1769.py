n = input()


def sol(n, c=0):
    s = 0
    if int(n) < 10:
        print(c)
        if int(n) % 3 == 0:
            print('YES')
        else:
            print('NO')
        return
    for i in n:
        s += int(i)
    sol(str(s), c+1)


sol(n)
