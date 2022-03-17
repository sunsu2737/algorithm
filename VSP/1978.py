n = int(input())

n_list = list(map(int,input().split()))


prime = [0]*1001

prime[0] = 1
prime[1] = 1

for i in range(2,1001):
    if prime[i]==0:
        for j in range(i*2,1001,i):
            prime[j]=1

cnt = 0

for i in n_list:
    if prime[i]==0:
        cnt+=1

print(cnt)