import sys
sys.setrecursionlimit(10**6)
line = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    a = a % b
    return gcd(b, a)


n = int(line())

ss= []
ms = []
mm=[]
result_m = 0
result_s = 0
for i in range(n):
    s, m = map(int, line().split())
    g=gcd(s,m)
    s=s//g
    m=m//g
    ss.append(s)
    ms.append(m)
    mm.append(m)
    
    if result_m == 0:
        if len(ms) == 2:
            result_m = (ms[0]*ms[1])//gcd(ms[0], ms[1])
            ms = []
    else:
        result_m = (result_m*ms[0])//gcd(result_m, ms[0])
        ms = []

for i in range(n):
    ss[i]*=result_m//mm[i]

if ms:
    print(ss[0],ms[0])
else:

    result_s = gcd(ss[0],ss[1])

    for i in range(2,n):
        result_s=gcd(result_s,ss[i])

    print(result_s,result_m)
        
