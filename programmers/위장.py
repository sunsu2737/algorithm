from collections import Counter

def solution(clothes):
    answer = 1
    c = Counter([x[1] for x in clothes])
    print(c)
    for v in c.values():
        answer *= (v+1)
    answer -= 1
    return answer