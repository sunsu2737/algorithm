class Node:
    def __init__(self, x, number):
        self.x = x
        self.number = number
        self.left = None
        self.right = None
        self.check = 0


class B_tree:

    def __init__(self):
        self.root = None

    def make_tree(self, nodeinfo):
        for y, x, number in nodeinfo:
            self.insert_node(x, number)

    def insert_node(self, x, number):
        if self.root == None:
            self.root = Node(x, number)
            return
        cur_node = self.root
        while True:
            if cur_node.x > x:
                if cur_node.left == None:
                    cur_node.left = Node(x, number)
                    break
                else:
                    cur_node = cur_node.left
            elif cur_node.x < x:
                if cur_node.right == None:
                    cur_node.right = Node(x, number)
                    break
                else:
                    cur_node = cur_node.right

    def preorder(self):
        if self.root == None:
            return []
        result = []
        stack = [self.root]

        while stack:

            if stack[-1].check == 0:
                result.append(stack[-1].number)
                stack[-1].check = 1
            if stack[-1].left != None and stack[-1].left.check == 0:
                stack.append(stack[-1].left)
                continue
            else:
                if stack[-1].right != None and stack[-1].right.check == 0:
                    stack.append(stack[-1].right)
                    continue
                else:
                    stack.pop()
        return result

    def postorder(self):
        if self.root == None:
            return []
        result = []
        stack = [self.root]

        while stack:

            if stack[-1].left != None and stack[-1].left.check == 1:
                stack.append(stack[-1].left)
                continue
            else:
                if stack[-1].right != None and stack[-1].right.check == 1:
                    stack.append(stack[-1].right)
                    continue
                else:
                    if stack[-1].check == 1:
                        result.append(stack[-1].number)
                        stack[-1].check = 2
                    stack.pop()
        return result


def solution(nodeinfo):
    answer = []
    nodeinfo_sorted = []
    i = 1
    for x, y in nodeinfo:
        nodeinfo_sorted.append((-y, x, i))
        i += 1

    nodeinfo_sorted.sort()
    b_tree = B_tree()
    b_tree.make_tree(nodeinfo_sorted)
    answer.append(b_tree.preorder())
    answer.append(b_tree.postorder())
    return answer


print(solution([[5, 3], [11, 5], [13, 3], [3, 5], [
    6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
