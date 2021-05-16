def solution(skill, skill_trees):
    cnt=0
    for skill_tree in skill_trees:
        temp=''
        isok=True
        
        for i in skill_tree:
            if i in skill:
                temp=temp+i
        for i in range(len(temp)):
            if temp[i]!=skill[i]:
                isok=False
        if isok==True:
            cnt+=1
    return cnt