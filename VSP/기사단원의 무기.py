# 레벨 1?

def solution(number, limit, power):
    answer = 0

    for i in range(1,number+1):
        cnt = 0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt>limit:
            answer+=power
        else:
            answer+=cnt
    return answer