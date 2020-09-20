import sys



T=int(input())

for i in range(T):


    N=int(sys.stdin.readline())


    next=[]
    next.append('1')
    while next:

        S=next.pop()
        if len(S)>100:
            continue
        if int(S)%N==0:

            print(S)
            next.reset()
            break

        next.append(S+'0')

        next.append(S+'1')