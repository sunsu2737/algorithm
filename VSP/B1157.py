import sys
line=sys.stdin.readline

S=list(line().strip().upper())
dict={}
for i in S:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
bindo=list(dict.items())
bindo=sorted(bindo,key=lambda bindo:bindo[1],reverse=True)
if len(bindo)>1 and bindo[1][1]==bindo[0][1]:
    print('?')
else:
    print(bindo[0][0])