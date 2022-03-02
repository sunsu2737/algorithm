n = int(input())
gesu = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
hanoi = [a,b,c]
first_list = [(a[0],0),(b[0],1),(c[0],2)]

x,y,z = [i[1] for i in first_list]

def h(a_i,b_i,c_i,z,y,x,flag=0):
    count = 0
    answer = 0
    while a_i+1 < len(hanoi[z]):
        if hanoi[z][a_i]+1 != hanoi[z][a_i+1]:
            if hanoi[z][a_i]<hanoi[x][c_i]:
                h_result=h(b_i,a_i,c_i,y,z,x,1)
                answer+=h_result[1]
                count+=h_result[0]
            else:
                h_result=h(b_i,c_i,a_i,y,x,z,1)
                answer+=h_result[1]
                count+=h_result[0]
        count+=1
        a_i+=1
    count+=1
    if flag == 1:
        return (count,2**count-1)
    else:
        if b_i<
print(first_list[2][1]+1)
print(h(0,0,0,z,y,x))