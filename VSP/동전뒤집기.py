def solution(coin: list, k: int):
    change_1 = 0
    change_2 = 0
    coin2 = coin[::]
    
    left = 0
    right = k-1

    while right<len(coin):
        if coin[left]==0:
            change_1+=1
            for i in range(left,right+1):
                if coin[i]==1:
                    coin[i]=0
                else:
                    coin[i]=1
        if coin2[left]==1:
            change_2+=1
            for i in range(left,right+1):
                if coin2[i]==1:
                    coin2[i]=0
                else:
                    coin2[i]=1
        left+=1
        right+=1
    if 0 in coin and 1 in coin2:
        return -1
    elif 0 in coin:
        return change_2
    elif 1 in coin2:
        return change_1
    else:
        return min(change_1,change_2)



print(solution([0, 1, 1, 0, 1, 1], 3))
