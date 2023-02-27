"""
先序遍历        根 左 右
中序遍历        左 根 右
后序遍历        左 右 根

递归序， 每个节点会返回三次，也就是先，中，后序遍历三次打印的位置。

按层遍历        BFS 用队列 （通过设置flag的方式， 发现层的结束）
"""

"""
非递归形式：
1. 任何递归函数都可以改成非递归
2. 通过栈的形式
"""


def pre(node):
    if not node:
        return
    stack = [node]
    while stack:
        p = stack.pop()
        print(p.val)
        if p.right:
            stack.append(p.right)
        if p.left:
            stack.append(p.left)


def inorder(node):
    # 1. 栈顶有左节点就 入栈
    # 2. 弹出， 右节点入栈 返回 1
    if not node:
        return
    stack = [node]
    while stack:
        if stack[-1].left:
            stack.append(stack[-1].left)
        else:
            p = stack.pop()
            print(p.val)
            if p.right:
                stack.append(p.right)
    return


def postorder(node):
    # 左右根 根右左的逆序 或者 加个指针记录上次打印的位置。
    if not node:
        return
    h = node
    stack = [node]
    while stack:
        c = stack[-1]
        if c.left and h != c.left and h != c.right:
            stack.append(c.left)
        elif c.right and h == c.right:
            stack.append(c.right)
        else:
            print(c.val)
            h = c
    return


if __name__ == "__main__":
    pre(n2)
