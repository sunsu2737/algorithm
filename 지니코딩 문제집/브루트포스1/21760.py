import sys

input = sys.stdin.readline

def main():

    t = int(input())

    # for _ in range(t):
    #     n, m, k, d = map(int, input().split())

    #     b = d//(k * m * (m-1)//2 * n + n*(n-1)//2 *m*m)

    #     if b ==0:
    #         print(-1)
    #     else:
    #         print(b*(k * m * (m-1)//2 * n + n*(n-1)//2 *m*m))


    for _ in range(t):
        n, m, k, d = map(int, input().split())

        b = 1
        answer = 0
        while True:
            a = b*k

            total = a * m * (m-1)//2 * n + n*(n-1)//2 * b*m*m

            if total <= d:
                answer = max(answer, total)
            elif total > d:
                break
            b += 1
        if answer ==0:
            print(-1)
        else:
            print(answer)

main()