import sys
line=sys.stdin.readline

N=int(line())
tree=list(map(int,line().split()))
st=[]
while tree:
    t=tree.pop()
    if t==0:
        continue

    while st :
        if st[-1]==2 and t>=1:
            t-=1
            st.pop()
        elif st[-1]==1 and t>=2:
            t-=2
            st.pop()
        if t==1:
            if 2 in st:
                st.pop(st.index(2))
            break

        if t==0:
            break
    t=t%3
    if t!=0:
        st.append(t)


if st:
    print("NO")
    
else:
    
    print("YES")
            
        

    
