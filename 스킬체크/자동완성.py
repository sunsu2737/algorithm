class Node:
    def __init__(self,word):
        self.children = {}
        self.complete = False

class Tri:
    def __init__(self):
        self.root = Node('')
        self.answer = 0
    def make_tri(self, words):

        for word in words:
            cur = self.root
            for i,w in enumerate(word):
                cur.children.setdefault(w,[0,Node(w)])
                cur.children[w][0] += 1
                cur = cur.children[w][1]
                if i == len(word)-1:
                    cur.complete = True
                
    
    def auto_complete(self, cur , count = 1):
        
        for _,node in cur.children.items():
            if node[0]==1:
                self.answer+=count
                continue
            if node[1].complete:
                self.answer+=count
            self.auto_complete(node[1],count+1)





                


def solution(words):
    answer = 0
    trie = Tri()
    trie.make_tri(words)
    # print(trie.root.children)
    trie.auto_complete(trie.root)
    return trie.answer



print(solution(["go","gone","guild"]))