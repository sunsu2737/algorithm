import requests
from ast import literal_eval

response=requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-1.json')

data= literal_eval(response.text)

def hot_spot(start,end):
    cycle_map=[[0]*60 for _ in range(60) ]
    # re={}
    for i in range(start,end):
        for order in data[str(i)]:
            src_x=order[0]//60
            src_y=order[0]%60
            dst_x=order[1]//60
            dst_y=order[1]%60

            cycle_map[src_x][src_y]-=1
            cycle_map[dst_x][dst_y]+=1
            # if i+order[2] in re:
            #     re[i+order[2]].append([dst_x,dst_y])
            # else:
            #     re[i+order[2]]=[dst_x,dst_y]


    max_cycle=0
    max_spot=[]
    min_cycle=0
    min_spot=[]

    for i in range(60):
        for j in range(60):
            if max_cycle<cycle_map[i][j]:
                max_cycle=cycle_map[i][j]
                max_spot=[i,j]
            if min_cycle>cycle_map[i][j]:
                min_cycle=cycle_map[i][j]
                min_spot=[i,j]

    return (max_spot,min_spot)

print(hot_spot(0,240))
print(hot_spot(240,480))
print(hot_spot(480,720))
print()
response=requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-2.json')

data= literal_eval(response.text)

print(hot_spot(0,240))
print(hot_spot(240,480))
print(hot_spot(480,720))
print()
response=requests.get('https://grepp-cloudfront.s3.ap-northeast-2.amazonaws.com/programmers_imgs/competition-imgs/2021kakao/problem2_day-3.json')

data= literal_eval(response.text)
print(hot_spot(0,240))
print(hot_spot(240,480))
print(hot_spot(480,720))
print()

