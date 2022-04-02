def solution(distance, rang, times):
    answer = 0
    time_line = [[-1] for _ in range(distance+1)]
    rt = list(zip(rang, times))
    rt.sort()
    # print(rt)
    rang, times = [], []
    for i in rt:

        rang.append(i[0])
        times.append(i[1])
    # print(rang)
    for i in range(len(rang)):
        for j in range(rang[i][0], rang[i][1]+1):
            time_line[j] = times[i]

    for i in range(1, distance+1):
        # print(time_line[i], i)
        if time_line[i][0] != -1:
            j = i % (time_line[i][0]+time_line[i][1])
            # print(j)
            if 1 <= j <= time_line[i][0]:
                return i
    return i


print(solution(12,	[[7, 8], [4, 6], [11, 10]],	[[2, 2], [2, 4], [3, 3]]))
