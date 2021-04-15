import itertools
def prime(n):
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    return a
        
def solution(numbers):
    num=[]
    numlist=[]
    
    for i in range(1,len(numbers)+1):
        num.append(list(itertools.permutations(numbers,i)))
    for i in num:
        for j in i:
            numlist.append(''.join(j))
    numlist=list(set(map(int,numlist)))
    answer=[]
    primes=prime(9999999)
    
    for i in numlist:
        if primes[i]:
            answer.append(1)

    return len(answer)