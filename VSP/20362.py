import sys
input=sys.stdin.readline
n,nick=input().split()

d={}
n=int(n)
for _ in range(n):
    name,chat=input().split()
    if name==nick:
        if chat in d:
            print(d[chat])
        else:
            print(0)
        break
    else:
        if chat in d:
            d[chat]+=1
        else:
            d[chat]=1
