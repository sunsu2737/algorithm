def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


# def div(start, end, house):

#     if start == end:
#         return 999999

#     if end-start == 1:
#         return dist(house[start], house[end])
#     mid = (start + end) // 2

#     result = min(div(start,mid,house),div(mid,end,house))

#     x_candi = []

#     for i in range(start, end+1):
#         if (house[mid][0]-house[i][0]) < result:
#             x_candi.append(house[i])
    
#     x_candi.sort(key = lambda x: x[1])

#     for i in range(len(x_candi)-1):
#         for j in range(i+1,len(x_candi)):
#             if (x_candi[i][1]-x_candi[j][1])**2 < result:
#                 result = min(dist(x_candi[i],x_candi[j]),result)
#             else:
#                 break
#     return result


def solution(house):
    answer = 0
    
    house.sort()

    x_min = 999999999999
    for i in range(1,len(house)):
        x_min = min(x_min,dist(house[i],house[i-1]))


    house.sort(key = lambda x: x[1])
    y_min = 999999999999

    for i in range(1,len(house)):
        y_min = min(y_min,dist(house[i],house[i-1]))

    answer = min(x_min,y_min)
    
    return answer
