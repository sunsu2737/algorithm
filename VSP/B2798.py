import sys
line=sys.stdin.readline

N,M=map(int,line().split())
card=list(map(int,line().split()))
min=99999999
sum=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if M-(card[i]+card[j]+card[k])<min and M-(card[i]+card[j]+card[k])>=0:
                sum=card[i]+card[j]+card[k]
                min=abs(M-sum)
print(sum)

