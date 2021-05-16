def check(string):
    st=[]
    for i in string:
        if i=='(':
            st.append(i)
        else:
            if len(st)==0:
                return False
            if  st[-1]!='(':
                return False
            else:
                st.pop()
    if len(st)==0:
        return True


def solution(string):
    if string=='':
        return string
    o,c=0,0
    cut=0
    for i in range(len(string)):
        if string[i]=='(':
            o+=1
        else :
            c+=1
        if c==o:
            cut=i+1
            break
    u=string[:cut]
    v=string[cut:]
    if check(u):
        return u+solution(v)
    else:
        new_u=''
        
        for i in range(1,len(u)-1):
            if u[i]=='(':
                new_u+=')'
            else:
                new_u+='('
        return '('+solution(v)+')'+new_u