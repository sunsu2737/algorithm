def summ(n):
    cnt=0
    while n>0:
        cnt+=n%10
        n=int(n/10)

    return cnt

def solution(x):
    if x%summ(x)==0:
        return True
    else:
        return False