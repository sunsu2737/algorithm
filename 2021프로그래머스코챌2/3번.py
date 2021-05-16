def find_110(s,i):
    x,y=len(s)-3,len(s)
    while x>=i+1:
        if s[x:y]=='110':
            return (x,y)
        x-=1
        y-=1
    return (0,0)

def solution(ss):
    answer = []
    for s in ss:
        i,j=0,0
        cnt=0
        while j<len(s):
            if s[j]=='1':
                cnt+=1
                j+=1
            else:
                cnt=0
                j+=1
                i=j

            if cnt>=3:
                x,y=find_110(s,i)
                # print(x,y)
                if (x,y)!=(0,0):
                    
                    s=s[:i]+s[x:y]+s[i:x]+s[y:]

                    j=i+3
                    i=j
                    cnt=0
                    # print(j)
                else:
                    break
        answer.append(s)

    return answer

print(solution(["1110", "100111100", "0111111010"]))