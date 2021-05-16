def solution(n):
    answer = sorted(list(str(n)))
    answer.reverse()
    answer=int(''.join(answer))
    return answer