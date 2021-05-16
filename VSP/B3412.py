import sys
import math
line=sys.stdin.readline

T=int(line())

for _ in range(T):
    N=int(line())
    score=0
    for __ in range(N):
        x,y=map(int,line().split())
        dist=math.sqrt(x*x+y*y)
        if dist<=20:
            score+=10
        elif dist<=40:
            score+=9
        elif dist<=60:
            score+=8
        elif dist<=80:
            score+=7
        elif dist<=100:
            score+=6
        elif dist<=120:
            score+=5
        elif dist<=140:
            score+=4
        elif dist<=160:
            score+=3
        elif dist<=180:
            score+=2
        elif dist<=200:
            score+=1
    print(score)