n = int(input())
budgets = list(map(int, input().split()))
total = int(input())


start = 0

end = max(budgets)


def get_all_budget(mid):
    result = 0
    for budget in budgets:
        result += min(mid, budget)
    return result


while start <= end:
    mid = (start+end)//2
    all_budget = get_all_budget(mid)

    if all_budget < total:
        answer = mid

        start = mid+1
    elif all_budget>total:
        end = mid-1
    else:
        answer = mid
        break

print(answer)
