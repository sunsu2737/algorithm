arr=[
    [0,1,0,1,0,1,0,1],
    [0,0,0,0,0,1,0,0],
    [1,0,1,0,0,1,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,1],
    [0,1,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0],
]

answer={}
dd=[(1,0),(0,1),(0,-1),(-1,0)]


def next_xy(x,y):
    y+=1
    if y>=8:
        x+=1
        y=0
    return x,y
def sol(x,y,cnt):
    # print(answer)
    if x==7 and y==7:
        if cnt in answer:
            answer[cnt]+=1
        else:
            answer[cnt]=1
        return
    temp=0
    a,b=next_xy(x,y)
    if arr[x][y]==1:
        return sol(a,b,cnt)
    for d in dd:
        if 0<=x+d[0]<8 and 0<=y+d[1]<8:
            if arr[x+d[0]][y+d[1]]==2:
                temp=1
                break
    if answer.keys() and cnt+(64-(x*8+y+1))<max(list(answer.keys())):
        return
    if temp==0:
        arr[x][y]=2
        sol(a,b,cnt+1)
        arr[x][y]=0
    sol(a,b,cnt)
sol(0,0,0)
print('최대',max(answer.keys()),'명,',answer[max(answer.keys())],'가지')