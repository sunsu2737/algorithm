n, m = map(int, input().split())

trees = list(map(int, input().split()))

start = 0
end = max(trees)


def get_tree_hight(mid):
    result = 0
    for tree in trees:
        result += max(tree-mid, 0)
    return result


while start <= end:

    mid = (start+end)//2
    tree_hight = get_tree_hight(mid)
    if tree_hight >= m:
        answer = mid
        start = mid+1
    else:
        end = mid-1

print(answer)
