import sys
line=sys.stdin.readline

data,base=line().split()
base=int(base)
flag=0
result=0
for i in range(len(data)-1,-1,-1):
    if '0'<=data[i]<='9':
        result+=int(data[i])*(base**flag)
    else:
        result+=(ord(data[i])-ord('A')+10)*(base**flag)
    flag+=1
print(result)