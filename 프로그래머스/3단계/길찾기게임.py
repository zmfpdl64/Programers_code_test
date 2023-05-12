# 15시 7분
# https://school.programmers.co.kr/learn/courses/30/lessons/42892

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None


class BsTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, insertnode):
        if self.root is None:
            self.root = insertnode
            return
        node = self.root
        while True:
            if node.y < insertnode.y:
                if node.x < insertnode.x:
                    if node.right is not None and node.right.x > insertnode.x:
                        insertnode.left = node
                        insertnode.right = node.right
                        node.right = None
                    else:
                        insertnode.left = node
                else:
                    if node.left is not None and node.left.x < insertnode.x:
                        insertnode.right = node
                        insertnode.left = node.left
                        node.left = None
                    else:
                        insertnode.right = node
                break
                self.root = insertnode
            else:
                if node.x < insertnode.x:
                    if node.right is None:
                        node.right = insertnode
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = insertnode
                        break
                    else:
                        node = node.left

    def inorder(self):
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            res.append(node.value)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res


def solution(nodeinfo):
    answer = [[]]
    tree = BsTree()
    for i, node in enumerate(nodeinfo):
        x, y = node[0], node[1]
        tree.insert(Node(i + 1, x, y))
    a = tree.inorder()
    for i in a:
        print(i)

    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])