import numpy as np

def solution(n, left, right):
    answer=[]

    for i in range(left, right+1):
        r = i//n
        c = i%n
        rc = max(r,c)
        answer.append(rc%n+1)
    return answer










    # answer = []
    # arr = [[0]*n for _ in range(n)]
    # arr = np.array(arr)
    # for i in range(n):
    #     not_0 = arr +0
    #     not_0[i+1:n+1,0:n+1]=1
    #     not_0[0:n+1,i+1:n+1]=1
    #     arr[not_0 ==0] = i+1

    # arr = np.concatenate(arr,axis=None)
    # arr = arr[left:right+1]
    # answer= list(arr)
    # print(answer)
    # return answer

print(solution(3,2,5))