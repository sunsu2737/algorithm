import math

def solution(a, b, g, s, w, t):
    answer = 0
    tick=min(t)
    truck=[[0,0] for _ in range(len(g))]
    g_t=0
    s_t=0
    for i in range(len(g)):
        if g[i]!=0:
            if g_t<a:
                truck[i][0]=min(g[i],w[i],a-g_t)
                g[i]-=min(g[i],w[i],a-g_t)
                g_t+=truck[i][0]
        if s[i]!=0:
            if s_t<b:
                truck[i][1]+=min(s[i],w[i]-truck[i][0],b-s_t)
                s[i]-=min(s[i],w[i]-truck[i][0],b-s_t)
                s_t+=truck[i][1]
    
    while True:
        
        answer+=tick
        # print(a,b,truck,g,s)
        for i in range(len(g)):
            if answer%(2*t[i])==0:
                if g[i]!=0:
                    if g_t<a:
                        truck[i][0]=min(g[i],w[i],a-g_t)
                        g[i]-=min(g[i],w[i],a-g_t)
                        g_t+=truck[i][0]
                if s[i]!=0:
                    if s_t<b:
                        truck[i][1]+=min(s[i],w[i]-truck[i][0],b-s_t)
                        s[i]-=min(s[i],w[i]-truck[i][0],b-s_t)
                        s_t+=truck[i][1]
            elif answer%t[i]==0:
                a-=truck[i][0]
                b-=truck[i][1]
                g_t-=truck[i][0]
                s_t-=truck[i][1]
                truck[i]=[0,0]
        if a==0 and b==0:
            break

        
    return answer


print(solution(10, 10, [100], [100], [7], [10]))