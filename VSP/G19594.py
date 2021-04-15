t = int(input())
for i in range(t):
    input()
    h = list(map(int, input().split()))
    d = list(map(int, input().split()))
    hd = list(zip(d, h))
    c = 0
    hd.sort()
    time = 0
    answer = 99999999999999999
    m_idx=0
    print(hd)
    for idx,(d, h) in enumerate(hd) :
        time += h
        if c<max(time-d,0):
            c=max(time-d,0)
            m_idx=idx
    for j in range(idx+1):
        answer=min(answer,c-(hd[j][1]-1))
    print(answer)

