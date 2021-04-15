import collections
import operator

def solution(answers):
    
    answers=collections.deque(answers)
    answer = []
    
    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]
    i,j,k,m=0,0,0,0
    
    cnt1,cnt2,cnt3=0,0,0
    
    while answers:
        
        if supo1[i]==answers[m]:
            cnt1+=1
        if supo2[j]==answers[m]:
            cnt2+=1
        if supo3[k]==answers[m]:
            cnt3+=1
            
        answers.popleft()
        i+=1
        j+=1
        k+=1
        
        if i==5:
            i=0
        if j==8:
            j=0
        if k==10:
            k=0
    cnt={1:cnt1,2:cnt2,3:cnt3}
    cntsort=sorted(cnt.items(),key=operator.itemgetter(1))
    cntsort.reverse()
    answer.append(cntsort[0][0])
    if cntsort[0][1]==cntsort[1][1]:
        answer.append(cntsort[1][0])
        if cntsort[1][1]==cntsort[2][1]:
            answer.append(cntsort[2][0])
    answer.sort()
    
    return answer