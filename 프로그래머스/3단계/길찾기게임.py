# 15시 7분
# https://school.programmers.co.kr/learn/courses/30/lessons/42892

class Node:
    def __init__(self, x, y, value=None, left=None, right=None, parent=None):
        self.x = x
        self.y = y
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, node):
        # print('self :', self.x, self.y)
        # print('in node : ', node.x, node.y)
        if node.y < self.y:
            # print('smaller')
            if node.x < self.x:
                if self.left is None:
                    self.left = node
                    node.parent = self
                    # print('left')
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    node.parent = self
                    # print('right')
                else:
                    self.right.insert(node)
        else:  # 현재 들어온 노드가 해당 노드보다 클 때
            # print('bigger')
            if node.x > self.x:
                node.left = self  # 현재 노드 입력 노드의 자식 노드로 변경
                node.parent = self.parent  # 현재 노드의 부모 노드를 입력 노드의 부모로 저장
                self.parent = node  # 현재 노드의 부모 노드를 입력 노드로 변경
                # print('self left')
                if self.right is not None and self.right.x > node.x:
                    node.right = self.right
                    self.right.parent = node
                    self.right = None
                    # print(node.x, node.y, " left : right", self.right.x, self.right.y)

            else:
                node.right = self
                node.parent = self.parent
                self.parent = node
                # print('self right')
                if self.left is not None and self.left.x < node.x:
                    node.left = self.left
                    self.left.parent = node
                    self.left = None
        return

    def preorder(self, node, res):
        # print(node.x, node.y)
        res.append(node.value)
        if node.left is not None:
            node.preorder(node.left, res)
        if node.right is not None:
            node.preorder(node.right, res)

    def inorder(self, node, res):
        if node.left is not None:
            node.inorder(node.left, res)
        # print(node.x, node.y)
        res.append(node.value)
        if node.right is not None:
            node.inorder(node.right, res)

    def postorder(self, node, res):
        if node.left is not None:
            node.postorder(node.left, res)
        if node.right is not None:
            node.postorder(node.right, res)
        # print(node.x, node.y)
        res.append(node.value)


def solution(nodeinfo):
    answer = [[]]
    pre = []
    post = []
    for i, value in enumerate(nodeinfo):
        nodeinfo[i] = [value[0],value[1],i+1]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    node1 = Node(nodeinfo[0][0], nodeinfo[0][1], nodeinfo[0][2])
    for i in range(1, len(nodeinfo)):
        x, y, v = nodeinfo[i]
        node1.insert(Node(x, y, v))
    node1.preorder(node1, pre)
    node1.postorder(node1, post)
    return [pre, post]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))