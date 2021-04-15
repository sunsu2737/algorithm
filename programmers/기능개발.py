# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
import math
def solution(pr, sp):
    com=[]
    for i in range(len(pr)):
        com.append(math.ceil((100-pr[i])/sp[i]))
    answer=[]
    num=0
    check=com[0]
    for i in range(len(com)):
        if com[i]<=check:
            num+=1
        else:
            answer.append(num)
            num=1
            check=com[i]
    answer.append(num)
    return answer