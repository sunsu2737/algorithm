n, k = map(int, input().split())

basket = [i for i in range(1, k+1)]


if sum(basket) > n:
    print(-1)
else:
    n -= sum(basket)
    i = len(basket)-1
    while n > 0:
        n -= 1
        basket[i] += 1
        i -= 1
        i %= len(basket)
    print(basket[-1]-basket[0])
