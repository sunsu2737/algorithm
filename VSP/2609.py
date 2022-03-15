
a, b = map(int, input().split())


if a < b:
    n, m = b, a
else:
    n, m = a, b


while m > 0:
    n, m = m, n % m

print(n)
print((a*b)//(n))
