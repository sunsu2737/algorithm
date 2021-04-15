n,m,b=map(int,input().split())

arr=[list(map(int,input().split())) for i in range(n)]
sum=b
for i in arr:
    for j in i:
        sum+=j
time=999999999999999999999999
answer=0

for i in range(257):
    cnt=0
    if i*n*m>sum:
        break
    for a in arr:
        for j in a:
            if j>i:
                cnt+=(j-i)*2
            else:
                cnt+=i-j
    if cnt<=time:
        time=cnt
        answer=i
print(time,answer)
                
