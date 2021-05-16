def up(cell,k,n,m):
    s=0
    for i in range(k-1,-1,-1):
        if cell[i]=='O':
            s+=1
        if s==m:
            return i
def down(cell,k,n,m):
    s=0
    for i in range(k+1,n):
        if cell[i]=='O':
            s+=1
        if s==m:
            return i
    return up(cell,k,n,m)

def solution(n, k, cmd):

    answer = ['O']*n
    stack=[]
    for c in cmd:
        if c=='C':
            stack.append(k)
            answer[k]='X'

            k=down(answer,k,n,1)
        elif c=='Z':
            answer[stack.pop()]='O'
        elif c[0]=='U':
                k=up(answer,k,n,int(c[2:]))
        elif c[0]=='D':
                k=down(answer,k,n,int(c[2:]))
    return ''.join(answer)