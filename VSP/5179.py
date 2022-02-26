T = int(input())

for t in range(T):
    m, n, p = map(int, input().split())
    check = [set() for i in range(p)]
    answer = [i for i in range(1, p+1)]
    score = [0]*p
    wrong = [dict() for i in range(p)]

    for i in range(n):
        a, b, c, d = input().split()
        a, c, d = map(int, [a, c, d])

        if b not in check[a-1]:
            if d == 1:

                check[a-1].add(b)
                score[a-1] += wrong[a-1][b]*20 + c if b in wrong[a-1] else c
                
            else:

                if b in wrong[a-1]:
                    wrong[a-1][b] += 1
                else:
                    wrong[a-1][b] = 1
        # print(wrong)
    answer.sort(key=lambda x: score[x-1])
    answer.sort(key=lambda x: len(check[x-1]), reverse=True)
    print(f'Data Set {t+1}:')
    for ans in answer:
        print(ans, len(check[ans-1]), score[ans-1])
    print()
