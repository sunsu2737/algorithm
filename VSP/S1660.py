import sys
line = sys.stdin.readline

def main():
    N = int(line())

    flag = 1
    temp = 3
    temp2 = 3
    t = []
    cnt=1
    while flag <= 300000:
        t.append(flag)
        flag += temp
        temp += temp2
        temp2 += 1

    tset=set(t)
    if N in tset:
        print(cnt)
        return
    while True:

        dp = set()
        for j in t:
            for i in tset: 
                if j+i<=N:
                    dp.add(j+i)
            if N in dp:
                print(cnt+1)
                return
        cnt+=1
        tset=dp

main()