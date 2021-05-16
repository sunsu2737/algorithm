def solution(n):
    cnt=0
    while n>0:
        cnt+=n%10
        n=int(n/10)

    return cnt