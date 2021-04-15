# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
from itertools import *
def solution(brown, red):
    brsum=[]
    for i in range(1,brown+red+1):
        if (brown+red)%i==0 and (brown+red)/i>=i:
            brsum.append([int((brown+red)/i),i])
            
    
    answer=[]
    for i in brsum:
        if i[0]*i[1]==brown+red and (i[0]-2)*(i[1]-2)==red :
            answer=list(i)
            break
    return answer