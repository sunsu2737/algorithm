def solution(s):
    r = []
    for c in s:
        if c == "(":
            r.append(c)
        else:
            if len(r):
                r.pop()
            else:
                return False
    return False if len(r) else True