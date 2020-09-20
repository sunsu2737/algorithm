import sys
line=sys.stdin.readline
rule=['E','A','B','C','D']
for i in range(3):
    a=list(map(int,line().split()))
    cnt=0
    for i in a:
        if i==0:
            cnt+=1
    print(rule[cnt])