import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().strip()
    lp, rp = 0, len(string)-1
    flag = 0
    while lp < rp:
        if string[lp] != string[rp]:
            flag = 1
            new_lp, new_rp = lp+1, rp
            while new_lp < new_rp:
                if string[new_lp] != string[new_rp]:
                    flag = 2
                    break
                new_lp += 1
                new_rp -= 1

            if flag == 2:
                flag = 1
                new_lp, new_rp = lp, rp-1
                while new_lp < new_rp:
                    if string[new_lp] != string[new_rp]:
                        flag = 2
                        break
                    new_lp += 1
                    new_rp -= 1
        if flag != 0:
            break
        lp += 1
        rp -= 1
    print(flag)
