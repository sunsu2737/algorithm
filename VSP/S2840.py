n, k = map(int, input().split())


def solve():
    arr = ['?']*n
    index = 0
    result = ''
    for i in range(k):
        num, s = input().split()
        index = (index+int(num)) % n
        for j in range(len(arr)):
            if j==index:
                continue
            if arr[j]==s:
                return '!'
        if arr[index] == '?':
            arr[index] = s
        elif arr[index] != '?' and arr[index] != s:
            return '!'
        

    for i in range(n):
        result += arr[index]

        index -= 1
    return result


print(solve())