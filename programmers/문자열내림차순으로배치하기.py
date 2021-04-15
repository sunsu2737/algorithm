def solution(s):
    lists=list(s)
    lists.sort()
    lists.reverse()
    answer=''.join(lists)
    return answer