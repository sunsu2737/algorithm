def solution(x, n):
    answer = []
    y=x
    for i in range(n):
        answer.append(y)
        y=y+x
    return answer