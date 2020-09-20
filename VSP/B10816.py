import sys
line=sys.stdin.readline

N=int(line())

cards=list(map(int,line().split()))

n=int(line())

find=list(map(int,line().split()))
dic={}


for i in cards:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
answer=[]
for i in find:
    if i in dic:
        answer.append(dic[i])
    else:
        answer.append(0)
print(*answer)