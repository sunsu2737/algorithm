def solution(people, limit):
    people.sort() #정렬
    length=len(people) #사람 수
    i=0 #가벼운 사람의 인덱스
    heavy=length-1 #무거운 사람의 인덱스
    count=0 #짝 지은 수
    while(i<heavy): #가벼운 사람과 무거운 사람이 겹치기 전까지 반복
        if people[i]+people[heavy]<=limit: #가벼운 사람과 무거운 사람의 무게를 합한 것이 구명보트 무게 제한보다 작거나 같다면
            count+=1 #짝을 만듦
            i+=1 #그 다음 가벼운 사람
            heavy-=1 #그 다음 무거운 사람
        else: #짝을 못 만들었으므로 무거운 사람은 혼자 태우고
            heavy-=1 #다음 무거운 사람으로 이동
    return length-count #전체 인원 수에서 짝의 수를 빼면 구명 보트 사용 횟수가 나옴