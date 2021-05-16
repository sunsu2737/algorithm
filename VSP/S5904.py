import sys

line = sys.stdin.readline

n=int(line())


num=0
while True:
    if num-1==n:
        print('m')
        break
    elif num-1>n:
        print('o')
        break
    num=(num+2)*2