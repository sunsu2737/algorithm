
def sum_list(a):                # 리스트 합
    pa=0
    for i in a:
        pa+=i
    return pa


def sum_2list(a,b):             # 두 리스트의합
    pa=sum_list(a)
    pa2=sum_list(b)

 
    return pa+pa2

def mycount(a,b):               # 두리스트의 원소개수의 합
    a_len=len(a)
    b_len=len(b)
    total_len=a_len+b_len

    return total_len

def calc_avg(pa,total_len):     # 합과 갯수로 평균을 구함
    return pa/total_len

def make_avg(a,b):              # 두리스트의 평균을 구함
    total_len=mycount(a,b)
    pa=sum_2list(a,b)
    avg=calc_avg(pa,total_len)
    
    return avg

a=[1,2,3]
b=[2,3,4]

avg=make_avg(a,b)


print(avg)
