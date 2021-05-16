import sys
line=sys.stdin.readline

N=int(line())
op=[]
num=[]
for _ in range(N):
    a,b=line().split()
    op.append(a)
    num.append(int(b))
cnt=0
for j in range(1,101):
    ans=j
    for i in range(N):
        if op[i]=='ADD':
            ans=ans+num[i]
        elif op[i]=='SUBTRACT':
            ans=ans-num[i]
        elif op[i]=='DIVIDE':
            ans=ans/num[i]
        elif op[i]=='MULTIPLY':
            ans=ans*num[i]

        if ans<0 or ans%1!=0:
            cnt+=1
            break
print(cnt)