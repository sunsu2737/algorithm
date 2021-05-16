n=int(input())
k=int(input())

answer=set()

card=[input() for i in range(n)]

def sol(s,idx,deep=0):
    if deep==k:
        answer.add(s)
        return
    for i in range(n):
        if i not in idx:
            idx.append(i)
            sol(s+card[i],idx,deep+1)
            idx.pop()
sol('',[])
# print(answer)
print(len(answer))
