from itertools import combinations


def solution(relation):
    col = len(relation[0])
    row = len(relation)
    atri = [i for i in range(col)]

    all_candi = []
    for i in range(1, col+1):
        all_candi.extend(list(combinations(atri, i)))

    unique_candi = []

    for candi in all_candi:
        keys = set()
        for r in relation:
            key = ''
            for i in candi:
                key += r[i]
            keys.add(key)
        if len(keys) == row:
            unique_candi.append(set(candi))
    del_candi=set()
    for stand in unique_candi:
        for cur in unique_candi:
            if stand.issubset(cur) and stand!=cur:
                del_candi.add(tuple(cur))
    
                


    return len(unique_candi)-len(del_candi)


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
         "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))