def fact(i):
    if i == 0:
        return 1
    return fact(i-1)*i


print(fact(4))
