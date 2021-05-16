import sys
line = sys.stdin.readline

word = line().strip()
pr=0
while word!='고무오리 디버깅 끝':
    word=line().strip()
    if word=='문제':
        pr+=1
    elif word=='고무오리':
        if pr>0:
            pr-=1
        else:
            pr+=2
if pr>0:
    print('힝구')
else:
    print('고무오리야 사랑해')