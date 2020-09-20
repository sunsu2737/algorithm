import math
a,b,c=map(int,input().split())

a=a*a

d=a/(b*b+c*c)

print(int(math.sqrt(d*b*b)),int(math.sqrt(d*c*c)))
