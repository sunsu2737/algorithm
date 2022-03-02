def solution(a):
    answer = []
    for i in a:
        if 'b' not in i:
            answer.append(True)
        else:
            left_b=i.find('b')
            right_b=i.rfind('b')
            # print(left_b,right_b)
            i=i[left_b:right_b+1]
            # print(i)
            b_cnt=0
            flag=0
            x,y=0,len(i)-1
            t=0
            while x<=y:
                # print(i[x:y+1])
                # print(b_cnt)

                if i[x]=='a':
                    if t==0 and b_cnt%i[x:y+1].count('a')!=0:
                        answer.append(False)
                        flag=1
                        break
                    t=1
                    x+=1
                    b_cnt=0
                    continue
                if i[y]=='a':
                    if t==0 and b_cnt%i[x:y+1].count('a')!=0:
                        answer.append(False)
                        flag=1
                        break
                    t=1
                    y-=1
                    b_cnt=0
                    continue
                if i[x]=='b' and i[y]=='b':
                    x+=1
                    y-=1
                    t=0
                    
                    b_cnt+=1
                    continue
            if flag==0 and t==1:
                answer.append(True)
            elif flag==0 and t==0:
                answer.append(False)
                
    return answer


a=["abab","bbaa","bababa","bbbabababbbaa"]
print(solution(a))