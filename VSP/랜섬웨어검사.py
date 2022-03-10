# 전 탐색

def solution(data, virus, k):
    answer = 0
    for i in range(len(data)-len(virus)+1):
        temp = 0
        for j in range(len(virus)):
            if data[i+j] != virus[j]:
                temp+=1
        if temp<=k:
            answer+=1

            
    return answer


# lcs
# 똑같은 시간초과 파이썬으로 못푸는듯
def solution(data, virus, k):
    answer = 0
    table = [[0]* (len(data)+1) for _ in range(len(virus)+1)]

    for i in range(len(virus)):
        for j in range(len(data)):
            if virus[i] != data[j]:
                table[i+1][j+1] = table[i][j] + 1
            else:
                table[i+1][j+1] = table[i][j]
                
    for i in range(len(virus),len(table[0])):
        
        if table[-1][i]<=k:
            answer+=1
    
    return answer