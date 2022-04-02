n = 1000 - int(input())

money = [500,100,50,10,5,1]
answer=0

for m in money:
    answer+=n//m
    n = n%m

print(answer)