# def solution(absolutes, signs):
#     answer=0
#     for i in range(len(signs)):
#         if signs[i]:
#             answer+=absolutes[i]
#         else:
#             answer-=absolutes[i]
#     return answer




# def solution(s):
#     m=s
#     answer = 0
#     open={')':'(','}':'{',']':'['}
#     for a in range(len(s)):
#         st=[]
#         for i in s:
#             if not i in open.keys():
#                 st.append(i)
#             else:
#                 if st and st[-1]==open[i]:
#                     st.pop()
#                 else:
#                     s=s[1:]+s[0]
#                     break
#         else:
#             if not st:
#                 answer+=1
#                 s=s[1:]+s[0]
#             else:

#                 s=s[1:]+s[0]
        
#     return answer
# import sys
# sys.setrecursionlimit(10**6)
# answer=0
# check=set()
# root=0
# def dfs(edge,node,a,p):
#     global answer
#     check.add(node)
#     for i in edge[node]:
#         if i not in check:
#             dfs(edge,i,a,node)
#     if node==root:
#         return

#     if a[node]>0:
#         answer+=a[node]
#         a[p]+=a[node]
#         a[node]=0
#     elif a[node]<0:
#         answer-=a[node]
#         a[p]+=a[node]
#         a[node]=0




# def solution(a, edges):
#     global root
#     max_child=0
#     tree=[(-1,-1)]*300001
#     edge={}
#     for i,j in edges:
#         if i in edge:
#             edge[i].add(j)
#         else:
#             edge[i]={j}
#         if j in edge:
#             edge[j].add(i)
#         else:
#             edge[j]={i}
#     # print(edge)
#     for k,v in edge.items():
#         if len(v)>max_child:
#             max_child=len(v)
#             root=k
#     dfs(edge,root,a,-1)
#     if a[root]==0:
#         return answer
#     return -1
# print(solution([-5,0,2,1,2],[[0,1],[3,4],[2,3],[0,3]]))
# from collections import deque
# def solution(n, z, roads, queries):
#     answer=[]
#     graph={}
#     for s,e,v in roads:
#         if s in graph:
#             graph[s].append([e,v])
#         else:
#             graph[s]=[[e,v]]

#     # print(graph)
#     for q in queries:
#         # print()
#         # print(q)
#         ans=q//z
#         qq=q%z
#         if qq==0:
#             answer.append(ans)
#             continue
#         next=deque()
#         if 0 in graph:
#             for n,v in graph[0]:
#                 if v<=qq:
#                     next.append([n,qq-v,ans+1,0])
#         for n in graph:
#             next.append([n,qq,ans+1,1])
#         while next:
            
#             n,q_q,a_ns,tp=next.popleft()
#             if q_q==0:
#                 answer.append(a_ns)
#                 break
#             if n in graph:
#                 for nn,v in graph[n]:
#                     if v<=q_q:
#                         next.append([nn,q_q-v,a_ns+1,0])
#             if tp==0:
#                 for nn in graph:
#                     next.append([nn,q_q,a_ns+1,1])

#         else:
#             if q<z:
#                 answer.append(-1)
#                 continue
#             ans=q//z-1
#             qq=q%z+z
#             next=deque()
#             if 0 in graph:
#                 for n,v in graph[0]:
#                     if v<=qq:
#                         next.append([n,qq-v,ans+1,0])
#             for n in graph:
#                 next.append([n,qq,ans+1,1])
#             while next:
#                 # print(next)
#                 n,q_q,a_ns,tp=next.popleft()
#                 if q_q==0:
#                     answer.append(a_ns)
#                     break
#                 if n in graph:
#                     for nn,v in graph[n]:
#                         if v<=q_q:
#                             next.append([nn,q_q-v,a_ns+1,0])
#                 if tp==0:
#                     for nn in graph:
#                         next.append([nn,q_q,a_ns+1,1])
#             else:
#                 answer.append(-1)


#     return answer

def dfs(n,roads,q,deepth,cnt):
    if deepth==n:
        if q==0:
            return cnt
        else:
            return -1
    dfs(n,roads,q,deepth+1)
    for i in range(deepth+1,len(roads)):
        if roads[i][0]==deepth and roads[i][2]<=q:
            dfs(n,roads,q-r[0],deepth+1,cnt+1)





def solution(n, z, roads, queries):
    answer = []
    roads.sort(key=lambda x:x[2],reverse=True)
    for q in queries:
        qq=q
        for r in roads:



    return answer

print(solution(5,5,[[1,2,3],[0,3,2]],[0,1,2,3,4,5,6]))