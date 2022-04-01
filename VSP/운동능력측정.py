import bisect
def solution(tests):
    answer = []
    tests = list(map(list, zip(*tests)))

    for test in tests:
        test.sort()
        pre_i = 1
        pre = 999999999999
        t_sum = [0]
        for i in range(len(test)):
            t_sum.append(t_sum[-1]+test[i])
        # print(test)
        # print(t_sq)
        for i in range(1, 1001):
            point = bisect.bisect_left(test,i)
            temp =  (i*point) - t_sum[point] + t_sum[-1] - t_sum[point] - (len(test)-point)*i
            # print(i,temp)
            if pre <= temp:
                answer.append(pre_i)
                break
            else:
                pre = temp
                pre_i = i

    return answer


print(solution([[59, 27], [45, 47], [45, 50]]))
