from collections import deque


def solution(gene, virus, k):
    answer = set()

    g = deque(gene[:len(virus)+k])

    virus = ' '+virus
    p = 0

    while True:
        g.appendleft(' ')
        print(g)
        table = [[0]*len(g) for i in range(len(virus))]

        for i in range(len(table[0])):
            table[0][i] = i
        for i in range(len(table)):
            table[i][0] = i
        for i in range(1, len(virus)):
            for j in range(1, len(g)):
                if g[j-1] != virus[i-1]:
                    table[i][j] = min(table[i-1][j-1], table[i-1]
                                      [j], table[i][j-1])+1
                else:
                    table[i][j] = table[i-1][j-1]

        for i in table:
            print(*i)
        print()
        for i in range(1, len(g)):
            if table[-1][i] <= k:
                answer.add(i+p)
        if len(virus)+k+p-1 >= len(gene):
            break
        g.popleft()
        g.popleft()
        g.append(gene[len(virus)+k+p-1])
        p += 1

    return sorted(list(answer))


print(solution("TAGGAT",	"AGT",	1))
