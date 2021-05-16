import sys


class Node:


    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        node=Node(data)
        if self.root is None:
            self.root=node
            return
        else:
            temp=self.root
            while True:
                parrent=temp
                if temp.data>data:
                    temp=temp.left
                    if temp is None:
                        parrent.left=node
                        return
                else :
                    temp = temp.right
                    if temp is None:
                        parrent.right = node
                        return

    def postorder(self, node):
        s = []
        while True:
            while node:
                if node.right:
                    s.append(node.right)
                s.append(node)
                node = node.left
            node = s.pop()
            if node.right and (s[-1] if len(s) else None) == node.right:
                s.pop()
                s.append(node)
                node = node.right
            else:
                print(node.data)
                node = None
            if not s:
                break
Btree=tree()

for num in sys.stdin:

    N=int(num)
    Btree.insert(N)
if Btree.root is not None:
    Btree.postorder(Btree.root)