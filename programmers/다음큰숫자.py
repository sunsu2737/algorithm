def solution(n):
    r = n + 1
    ct = bin(n).count("1")
    while True:
        if bin(r).count("1") == ct:
            return r
        r += 1