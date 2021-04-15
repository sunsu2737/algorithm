cd=input()
cnt=0

def sol(n='',deep=0):
    global cnt
    if deep==len(cd):
        cnt+=1
        return
    if cd[deep]=='c':
        for i in range(ord('a'),ord('z')+1):
            if deep==0:
                sol(n+chr(i),deep+1)
            else:
                if n[-1]!=chr(i):
                    sol(n+chr(i),deep+1)
    else:
        for i in range(10):
            if deep==0:
                sol(n+str(i),deep+1)
            else:
                if n[-1]!=str(i):
                    sol(n+str(i),deep+1)

sol()
print(cnt)