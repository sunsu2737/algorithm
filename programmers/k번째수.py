def solution(array, commands):
    answer = []
    idx=0
    while True:
        i,j,k=commands[idx]
        arrayt=array[i-1:j]
        arrayt.sort()
        answer.append(arrayt[k-1])
        idx=idx+1
     
        if idx == len(commands):
            break
    
    return answer