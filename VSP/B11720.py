import sys
line=sys.stdin.readline

N=line()
numberList=list(line().strip())
sum=0
for i in numberList:
    sum+=int(i)
print(sum)
