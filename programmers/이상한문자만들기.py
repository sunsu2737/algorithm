def solution(s):
    s = s.replace(' ', '.,.')

    lists = s.split('.')

    for i in range(len(lists)):
        lists[i] = list(lists[i])

    for i in range(len(lists)):
        for j in range(len(lists[i])):
            if j % 2 == 0:
                lists[i][j] = lists[i][j].upper()
            elif j % 2 == 1:
                lists[i][j] = lists[i][j].lower()

    for i in range(len(lists)):
        lists[i] = ''.join(lists[i])

    answer = ''.join(lists)
    answer = answer.replace(',', ' ')
    return answer