T=int(input())

A=T//300
T=T%300
B=T//60
T=T%60
C=T//10
T=T%10
if T!=0:
    print(-1)
    exit(0)
print(A,B,C)