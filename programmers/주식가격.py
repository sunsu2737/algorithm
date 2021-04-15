def solution(prices):
    answer=[]
    for i in range(len(prices)):
        count=0
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                count+=1
                break
            else:
                count+=1
        answer.append(count)
    return answer