

T = int(input())


def get_postorder(root, preorder, inorder):
    left = []
    right = []
    flag = True
    # print(inorder)
    if len(inorder) == 1:
        print(inorder[0], end=' ')
        return
    elif len(inorder) < 1:
        return
    for i in inorder:
        if flag:
            if i == root:
                flag = False
            else:
                left.append(i)
        else:
            right.append(i)

    leftpre = preorder[1:len(left)+1]
    rightpre = preorder[len(left)+1:]
    if len(leftpre)>=1:
        get_postorder(leftpre[0], leftpre, left)
    if len(rightpre)>=1:
        get_postorder(rightpre[0], rightpre, right)
    print(root, end=' ')


for _ in range(T):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    get_postorder(preorder[0], preorder, inorder)
    print()
