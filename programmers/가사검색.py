#TODO:다시풀기 (시간초과)

class Node:

    def __init__(self, w=""):
        self.w = w
        self.child = {}
        self.length = 0


class Tri:

    def __init__(self):
        self.root = Node("")
        self.keyList = {}

    def creat(self, words, reverse=False):

        for word in words:

            if reverse:
                word = word[::-1]
            if word not in self.keyList:
                self.keyList[word] = len(word)
                cur_node = self.root

                for w in word:
                    if w not in cur_node.child:
                        cur_node.child[w] = Node(w)
                    cur_node = cur_node.child[w]
                cur_node.length = len(word)

    def search(self, word):
        cur_node = self.root
        word_len = len(word)
        cnt = 0
        dest = word.count('?')
        stack = []
        deepth=0
        for w in word:
            if w != '?':
                if w not in cur_node.child:
                    return 0
                cur_node = cur_node.child[w]
                deepth+=1
            else:
                if word_len == dest:
                    for i in self.keyList.values():
                        if word_len == i:
                            cnt += 1
                    return cnt
                else:
                    stack.append((cur_node, deepth))
                    while stack:
                        cur_node, deepth = stack.pop()
                        if deepth == word_len:
                            if cur_node.length ==word_len:
                                cnt += 1
                        else:
                            for next_node in cur_node.child.values():
                                stack.append((next_node, deepth+1))
                    return cnt


def solution(words, queries):
    answer = []
    dp={}
    tri = Tri()
    r_tri = Tri()
    tri.creat(words)
    r_tri.creat(words, True)

    for word in queries:
        if word not in dp:
            if word[0] == '?':
                answer.append(r_tri.search(word[::-1]))
            else:
                answer.append(tri.search(word))
            dp[word]=answer[-1]
        else:
            answer.append(dp[word])
    return answer