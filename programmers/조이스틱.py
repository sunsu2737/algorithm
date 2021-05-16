def solution(name):
    cnt=0
    idx=0
    name=list(name)
    aset=['A' for i in range(len(name))]
    while True:
        lidx,ridx=idx,idx
        if name==aset:
            break
        if name[idx]!=aset[idx]:
            val=ord(name[idx])-ord(aset[idx])
            aset[idx]=name[idx]
            if val>=13:
                cnt+=26-val
            else:
                cnt+=val
        else:
            while True:
                lidx-=1
                ridx+=1
                if name[ridx]!=aset[ridx]:
                    cnt+=ridx-idx
                    idx=ridx
                    break
                elif name[lidx]!=aset[lidx]:
                    cnt+=idx-lidx
                    idx=lidx
                    break
                
    return cnt