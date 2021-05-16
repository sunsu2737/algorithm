import sys
input=sys.stdin.readline
n=int(input())
arr=[list(map(int,input().split())) for  _ in range(n)]
arr.append(arr[0])
row_line={}
col_line={}

pre_x=arr[0][0]
pre_y=arr[0][1]

for i in range(1,len(arr)):
    x=arr[i][0]
    y=arr[i][1]
    start_x=min(x,pre_x)
    end_x=max(x,pre_x)
    start_y=min(y,pre_y)
    end_y=max(y,pre_y)
    if pre_x==x:
        if start_y in row_line:
            row_line[start_y]+=1
        else:
            row_line[start_y]=1
        if end_y in row_line:
            row_line[end_y]-=1
        else:
            row_line[end_y]=-1
    if pre_y==y:
        if start_x in col_line:
            col_line[start_x]+=1
        else:
            col_line[start_x]=1
        if end_x in col_line:
            col_line[end_x]-=1
        else:
            col_line[end_x]=-1    
    pre_x=x
    pre_y=y





col=sorted(col_line.items(),key= lambda x:x[0])
row=sorted(row_line.items(),key= lambda x:x[0])

h=0
answer=0
for i,v in col:
    h+=v
    answer=max(answer,h)
h=0
for i,v in row:
    h+=v
    answer=max(answer,h)
print(answer)