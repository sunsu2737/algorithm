x, y = map(int, input().split())


z = y*100//x  


start = 1

end = 100000000000


def get_per(win):
    return (y+win)*100 // (x+win) 


answer = 0

while start <= end:

    mid = (start+end)//2

    if get_per(mid) > z:
        answer = mid   # answer = 10
        end = mid-1
    else:
        start = mid+1

if answer==0:
    print(-1)
else:
    print(answer)

