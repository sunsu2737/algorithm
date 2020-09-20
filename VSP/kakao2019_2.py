def solution(N, stages):
    answer = []
    stage = [0 for _ in range(N+2)]
    fail = [0 for _ in range(N+2)]
    fail_rate = []
    for s in stages:
        for i in range(1, s+1):
            stage[i] += 1
        fail[s] += 1
    for i in range(1, N+1):
        if stage[i]>0:
            fail_rate.append((fail[i]/stage[i], -i))
        else:
            fail_rate.append((0,-i))
    fail_rate.sort(reverse=True)

    answer = [-fail_rate[i][1] for i in range(N)]
    return answer


N = 5
stages = [1,2,3,4,4,4,4,4,4,4]
print(solution(N, stages))
