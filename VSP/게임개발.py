def solution(develop, design, least, most):
    answer = 0

    people = [(develop[i], design[i], design[i] - develop[i]) for i in range(len(develop))]

    people.sort(key = lambda x: (x[2],-x[0],-x[1]))

    cnt = 0
    for i in range(len(people)):
        if cnt<least:
            answer+=people[i][0]
            cnt+=1
        else:
            if cnt<most:
                if people[i][0]>people[i][1]:
                    answer+=people[i][0]
                    cnt+=1
                else:
                    answer+=people[i][1]
            else:
                answer+=people[i][1]



    return answer