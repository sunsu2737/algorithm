def solution(n, lost, reserve):
    
    reserveset= set(reserve)
    lostset=set(lost)
    reserveset2=reserveset-lostset
    lostset2=lostset-reserveset
    for i in lostset2:
        if i-1 in reserveset2:
            lostset2=lostset2-{i}
            reserveset2=reserveset2-{i-1}
        elif i+1 in reserveset2:
            lostset2=lostset2-{i}
            reserveset2=reserveset2-{i+1}
    cnt=len(lostset2)
    
            
    return n-cnt