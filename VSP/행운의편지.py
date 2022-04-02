

def spread(graph,check,n,c,k):
    
    flag = True
    while flag:
        flag=False
        for i in range(c+1,n+1):
            if check[i] >= k:
                check[i] = -1
                if i in graph:
                    
                    for j in graph[i]:
                        # print(i,j)
                        if check[j] != -1:
                            check[j] += 1 
                print()
                flag= True
        


def solution(n, c, k, contact):
    assert(1<=n<=10000)
    assert(1<=c<=n)
    assert(1<=k<=c)
    assert(1<=len(contact)<=n*(n-1))
    answer = 0

    graph = {}


    check = [0] * (n+1)
    

    for i in contact:
        assert(1<=i[0]<=n)
        assert(1<=i[1]<=n)
        assert(i[0]!=i[1])
        if i[0] in graph:
            graph[i[0]].append(i[1])
        else:
            graph[i[0]] = [i[1]]
        if i[1] in graph:
            graph[i[1]].append(i[0])
        else:
            graph[i[1]] = [i[0]]
    for i in range(1,c+1):
        check[i]=-1
        if i in graph:
            for j in graph[i]:
                # print(j)
                check[j]+=1
    # print(check)
    spread(graph,check,n,c,k)

    answer = check.count(0)-1


    return answer
