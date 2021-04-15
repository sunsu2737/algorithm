def solution(arr):
    amin=min(arr)
    
    for i in range(len(arr)):
        if arr[i]==amin:
            arr.remove(arr[i])
            break
    if arr==[]:
        arr=[-1]
    return arr