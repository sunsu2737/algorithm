def gcd(n,m):
    if n<m:
        n,m=m,n
    n=n%m
    if n==0:
        return m
    return gcd(n,m)
def solution(n, m):
    
    
    return [gcd(n,m),m*n/gcd(n,m)]