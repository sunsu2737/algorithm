
def solution(tests):
    answer = []
    tests = list(map(list, zip(*tests)))

    for test in tests:
        test.sort()
        pre = sum(test)
        ans = -1
        start = test[0]
        end = test[-1]+test[-1]-test[0]
        while start <= end:
            mid = (start + end)//2
            temp = 0
            for t2 in test:
                temp += abs(mid-t2)
            print(start, end, temp, mid, ans)
            if pre >= temp:
                end = mid-1
                ans = mid
                pre = temp

            else:
                start = mid+1
        answer.append(ans)
    return answer


print(solution([[59, 27], [45, 47], [45, 50]]))
