import sys
line=sys.stdin.readline

N=int(line())
st=[]
for _ in range(N):
    c=int(line())
    if c==0:
        st.pop()
    else:
        st.append(c)
print(sum(st))