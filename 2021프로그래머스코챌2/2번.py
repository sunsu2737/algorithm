
def solution(numbers):
    answer = []
    for i in numbers:
        b=bin(i)[2:]
        cnt=b.count('0')
        if b=='0':
            answer.append(1)
            continue
        if cnt==0:
            b=b.replace('1','0',1)
            b='1'+b
            answer.append(int(b,2))
            
        else:
            b=list(b)
            b=b[::-1]
            zero=b.index('0')
            one=b.index('1')
            if one<zero:
                b[zero]='1'
                b[zero-1]='0'
                
            else:
                b[zero]='1'
            answer.append(int(''.join(b[::-1]),2))
                
    return answer

print(solution([2,7,0]))