import sys
line = sys.stdin.readline

mo = ['a', 'e', 'i', 'o', 'u']


while True:
    passward = line().strip()
    if passward == 'end':
        break
    flag = 1
    for i in mo:
        if i in passward:
            flag = 0
            break
    cntja = 0
    cntmo = 0

    for i in passward:

        if i in mo:
            cntmo += 1
            cntja = 0
        else:
            cntja += 1
            cntmo = 0
        if cntmo >= 3 or cntja >= 3:
            flag = 1
            break
    for i in range(len(passward)-1):
        if passward[i] not in 'eo' and passward[i] == passward[i+1]:
            flag = 1
            break
    if flag == 1:
        print('<{0}> is not acceptable.'.format(passward))
    else:
        print('<{0}> is acceptable.'.format(passward))
