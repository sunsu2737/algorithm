def max_(a, b):
    return a <= b if len(a) == len(b) else a+b <= b+a


def quick_sort(arr):
    leng = len(arr)
    if leng <= 1:
        return arr
    else:
        pivot = arr[0]
        greater = [element for element in arr[1:] if max_(element, pivot)]
        lesser = [element for element in arr[1:] if not max_(element, pivot)]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


def solution(nums):
    if set(nums) == {0}:
        return "0"
    nums = [str(num) for num in nums]
    nums = quick_sort(nums)
    return "".join(nums)