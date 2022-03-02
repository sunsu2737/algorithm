from collections import deque
t=int(input())

for i in range(t):
    n,m,c=map(int,input().split())
    m_list={}
    elve={}
    elve_cnt=0
    for _ in range(c):
        a,b=map(int,input().split())
        if a!=b:
            if a in m_list:
                m_list[a].append(b)
            else:
                m_list[a]=deque([b])
    floor=1
    time=0
    up_down=1
    elve_max=0
    # print(m_list)
    while True:
        time+=1
        if floor in elve:
            elve_cnt-=elve[floor]
            del elve[floor]
        if floor in m_list:
            a=m_list[floor].popleft()
            if a in elve:
                elve[a]+=1
            else:
                elve[a]=1
            elve_cnt+=1
            if not m_list[floor]:
                del m_list[floor]
            if elve_cnt >m:
                # print('max')
                print(time)
                break
        elve_max=max(elve_max,elve_cnt)
        if elve_cnt==0 and not m_list:
            break
        floor+=up_down
        if floor>n:
            floor=n-1
            up_down=-1
        if floor<1:
            floor=1
            up_down=1
    if elve_cnt==0:
        print(elve_max-m)