def solution(record):
    answer = []
    users = {}
    event = []
    for r in record:

        commend = list(r.split())

        if commend[0] == 'Enter':
            event.append((commend[1], '님이 들어왔습니다.'))
            users[commend[1]] = commend[2]
        elif commend[0] == 'Leave':
            event.append((commend[1], '님이 나갔습니다.'))
        else:
            users[commend[1]] = commend[2]

    for e in event:
        answer.append(users[e[0]]+e[1])
    return answer