def solution(n, m, x, y, queries):
    start_x=[x,y]
    end_x=[x,y]
    queries.reverse()
    for com,dx in queries:
        print(start_x,end_x,end=' -> ')

        if com ==2:
            if start_x[0]==0 and end_x[0]>=0  :
                end_x[0]=min(end_x[0]+dx,n-1)
            else:
                end_x[0]=min(end_x[0]+dx,n-1)
                start_x[0]=start_x[0]+dx
        elif com ==3:
            if end_x[0]==n-1 and start_x[0]<n:
                start_x[0]=max(start_x[0]-dx,0)
            else:
                end_x[0]=end_x[0]-dx
                start_x[0]=max(start_x[0]-dx,0)
        elif com ==0:
            if start_x[1]==0 and end_x[1]>=0:
                end_x[1]=min(end_x[1]+dx,m-1)
            else:
                end_x[1]=min(end_x[1]+dx,m-1)
                start_x[1]=start_x[1]+dx
        elif com ==1:
            if end_x[1]==m-1 and start_x[1]<m:
                start_x[1]=max(start_x[1]-dx,0)
            else:
                end_x[1]=end_x[1]-dx
                start_x[1]=max(start_x[1]-dx,0)
        print(start_x,end_x)
    a=(end_x[0]-start_x[0]+1)
    b=(end_x[1]-start_x[1]+1)
    if a>0 and b>0:
        return a*b
    else:
        return 0
print(solution(3,3,0,1,[[1,2],[0,100],[2,100]]))