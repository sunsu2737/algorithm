def solution(enemy, ability):
    answer = 0

    ability.sort()
    enemy.sort()
    while enemy and ability:
        e = enemy.pop()
        a = ability.pop()

        if a>=e:
            answer+=1
        else:
            ability.append(a)
    return answer