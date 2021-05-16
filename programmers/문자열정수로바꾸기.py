def solution(s):
    ss=list(s)
    answer=0
    if ss[0]=='-':
        ss.remove(ss[0])
        answer=-int(''.join(ss))
    else:

        answer=int(''.join(ss))
    return answer