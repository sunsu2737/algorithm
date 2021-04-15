def solution(s, n):
    lists=[]
    answer=''
    for i in s:
        sn=ord(i)  
        
        for j in range(n):
            sn+=1
            if sn==123:
                sn=97
            elif sn==91:
                sn=65
            elif 57>sn>32:
                sn=32
        lists.append(sn)
    
    for i in range(len(lists)):
        lists[i]=chr(lists[i])
    answer=''.join(lists)
        
    
    return answer