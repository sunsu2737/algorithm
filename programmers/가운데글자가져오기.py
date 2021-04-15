def solution(s):
    s=list(s)
    idx=int(len(s)/2)
    if len(s)%2==0:
        answer=s[idx-1:idx+1]
    elif len(s)%2==1:
        answer=s[idx]
    return ''.join(answer)