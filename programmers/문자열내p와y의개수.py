def solution(s):
    s=s.lower()
    
    pcnt=0
    ycnt=0
    for i in s:
        if i=='p':
            pcnt+=1
        elif i=='y':
            ycnt+=1
    

    return pcnt==ycnt