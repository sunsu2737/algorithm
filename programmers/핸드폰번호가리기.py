def solution(p):
    lens=len(p)-4
    p=list(p)
    for i in range(lens):
        p[i]='*'
    return ''.join(p)