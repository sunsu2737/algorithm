import sys
sys.setrecursionlimit(10**6)
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))


def b_search(cards, target):
    start = 0
    end = len(cards)-1

    while end >= start:
        mid = (start+end)//2

        if cards[mid] > target:
            end = mid-1
        elif cards[mid] < target:
            start = mid+1
        else:
            return True
    return False

def b_search2(start,end,cards, target):
    mid = (start+end)//2

    if start>end:
        return False
    if cards[mid] > target:
        end = mid-1
        return b_search2(start,end,cards,target)
    elif cards[mid] < target:
        start = mid+1
        return b_search2(start,end,cards,target)
    else:
        return True

cards.sort()
for target in targets:
    print(1 if b_search2(0,n-1,cards, target) else 0, end=' ')
