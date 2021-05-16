def solution(s):
    try :
        ss=int(s)
    except ValueError:
        return False
    return len(s)== 4 or len(s)==6