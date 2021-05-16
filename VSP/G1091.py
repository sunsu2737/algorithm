import sys
line=sys.stdin.readline

N=int(line())
P=list(map(int,line().split()))
S=list(map(int,line().split()))

card=[i%3 for i in range(N)]
card2=[i%3 for i in range(N)]
def check():
    for i in range(N):
        if card[i]!=P[i]:
            return False
    return True
cnt=0

while True:
    flag=0
    if check():
        break
    for i in range(N):
        card2[i]=card[S[i]]
    for i in range(N):
        card[i]=card2[i]
    for i in range(N):
        if card[i]!=i%3:
            flag=1
            break
    if flag==0:
        print(-1)
        exit()
    cnt+=1
print(cnt)
