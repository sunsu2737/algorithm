def out(pool, sp):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        st = f'{i}{j}{k}{l}'
                        for s in sp:
                            if s in st:
                                pool.discard(st)


def judge(num1, num2, st, ba):
    s = 0
    b = 0
    # print(num1, num2)
    for i in range(4):
        if num1[i] == num2[i]:
            s += 1
        else:
            if num1[i] in num2:
                b += 1
    # print(s, b)
    return s == st and b == ba


def sb(pool, sp, strike, ball):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        st = f'{i}{j}{k}{l}'

                        if not judge(sp, st, strike, ball):
                            pool.discard(st)


def solution(speak, reply):
    answer = []
    pool = set()
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        pool.add(f'{i}{j}{k}{l}')
    total = len(pool)
    print(total)
    for idx in range(len(speak)):
        if reply[idx] == 'out':
            out(pool, speak[idx])
            answer.append(total-len(pool))
            total = len(pool)
        else:
            s = int(reply[idx][0])
            b = int(reply[idx][2])
            sb(pool, speak[idx], s, b)
            answer.append(total - len(pool))
            total = len(pool)
            # print(total)
    return answer


print(solution(["5796", "1234", "0846", "8064"],
      ["0S1B", "1S1B", "0S2B", "2S0B"]))
