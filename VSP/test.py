
# class Node:
#     def __init__(self, what):
#         self.what = what
#         self.child = {}
#         self.cnt = 0


# class Tree:
#     def __init__(self):
#         self.root = Node('')

#     def make_tree(self, info):
#         for i in info:
#             i = list(i.split())
#             cur_node = self.root
#             for j in i:
#                 if j.isdigit():
#                     j = int(j)
#                 if j in cur_node.child:
#                     cur_node = cur_node.child[j]
#                 else:
#                     cur_node.child[j] = Node(j)
#                     cur_node = cur_node.child[j]
#             cur_node.cnt += 1

#     def search(self, query):
#         result = []
#         for i in query:
#             i = list(i.split())
#             cur_node = self.root
#             cur = [cur_node]
#             next = []
#             for j in i:
#                 if j != 'and':
#                     if j.isdigit():
#                         j = int(j)
#                         cnt = 0
#                         for cur_node in cur:
#                             for point in cur_node.child:
#                                 if point >= j:
#                                     cnt += cur_node.child[point].cnt

#                         result.append(cnt)
#                         break
#                     while cur:
#                         cur_node = cur.pop()

#                         if j == '-':
#                             for node in cur_node.child.values():
#                                 next.append(node)
#                         else:
#                             if j in cur_node.child:
#                                 next.append(cur_node.child[j])
#                     cur = next.copy()
#                     next = []

#         return result


def solution(info, query):
    new_query = {}
    for q in query:
        q = list(q.replace(' and', '').split())
        new_query[tuple(q[0:4])]=[q[4],0]
    for i in info:
        i= tuple(i.split())
        flag=0
        if i[0:4] in new_query:
            if i[4] >=new_query[i[0:4]][0]:
                new_query[i[0:4]][1]+=1
                flag=1
        if flag==1:
            continue
        


            
    print(new_query)

    return


print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
      "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))
