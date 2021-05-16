n=int(input())
print(2**n-1)

def hanoi(s,p,e,n):
    if n==1:
        print(s,e)
        return
    hanoi(s,e,p,n-1)
    print(s,e)
    hanoi(p,s,e,n-1)

hanoi(1,2,3,n)