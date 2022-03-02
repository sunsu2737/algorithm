numbers=set()


def get_number(dice,deepth=0):


def solution(dice):
    answer = 0
    num_pool={1,2,3,4,5,6,7,8,9,0}
    dice=list(map(set,dice))
    min_numbers=[]
    for nums in dice:
        min_numbers.append(nums)
    min_numbers.sort()


    return answer


dice=[[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]
print(solution(dice))