from api import *



hot_spot={
    240:[[50,37],[59,55]],
    480:[[43,55],[12,4]],
    720:[[41,5],[16,9]]
}

def make_xy(id,size):
    x=id//size
    y=id%size
    return (x,y)

def get_distance(s,d):
    return abs(s[0]-d[0])+abs(s[1]-d[1])
# 0: 6초간 아무것도 하지 않음
# 1: 오른쪽으로 한 칸 이동
# 2: 아래로 한 칸 이동
# 3: 왼쪽으로 한 칸 이동
# 4: 위로 한 칸 이동
# 5: 자전거 상차
# 6: 자전거 하차
def solve1():
    auth_key=start_api(1)['auth_key']
    commands=[
        {'truck_id':0,'command':[2,1]},
        {'truck_id':1,'command':[2,2,2,1]},
        {'truck_id':2,'command':[2,2,1,1]},
        {'truck_id':3,'command':[2,1,1,1]},
        {'truck_id':4,'command':[2,2,2,1,1,1]}
        ]
    
        
    print(simulate_api(commands=commands,auth_key=auth_key).json())



    for _ in range(719):
        # bikes=location_api(auth_key)['locations']
        # dst=[]
        # src=[]
        # print(bikes)
        print(simulate_api(commands=[],auth_key=auth_key).json())
        # for bike in bikes:
        #     if bike['located_bikes_count']<=1:
        #         dst.append(make_xy(bike['id']))
        #     elif bike['located_bikes_count']>2:
        #         src.append(make_xy(bike['id']))
        # while dst:
        #     d=dst.pop()
        #     min_s=()
        #     min_distance=0
        #     for s in src:
        #         distance=get_distance(s,d)
        #         if distance<min_distance:
        #             min_distance=distance
        #             min_s=s

            
    print(score_api(auth_key))




    


solve1()

