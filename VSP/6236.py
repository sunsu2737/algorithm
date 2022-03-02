n,m = map(int,input().split())

money_list = [int(input()) for _ in range(n)]

start = 0
end = 10000



def check(money,money_list,m):
    count=1
    cur_m=money
    for mon in money_list:
        if money<mon:
            return False
        if cur_m>=mon:
            cur_m-=mon
        else:
            count+=1
            cur_m=money-mon

    return count<=m

answer=sum(money_list)

while start<=end:
    mid = (start+end)//2

    if check(mid,money_list,m):
        answer=mid
        end=mid-1
    else:
        start = mid+1


print(answer)