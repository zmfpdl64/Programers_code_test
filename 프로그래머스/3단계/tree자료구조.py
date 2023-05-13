

class Node:
    def __init__(self, x, y, left=None, right=None, parent=None):
        self.x = x
        self.y = y
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
        else: # 현재 들어온 노드가 해당 노드보다 클 때
            # print('bigger')
            if node.x > self.x:
                node.left = self # 현재 노드 입력 노드의 자식 노드로 변경
                node.parent = self.parent # 현재 노드의 부모 노드를 입력 노드의 부모로 저장
                self.parent = node # 현재 노드의 부모 노드를 입력 노드로 변경
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
    def preorder(self, node):
        print(node.x, node.y)
        if node.left is not None:
            node.preorder(node.left)
        if node.right is not None:
            node.preorder(node.right)
    def inorder(self, node):
        if node.left is not None:
            node.inorder(node.left)
        print(node.x, node.y)
        if node.right is not None:
            node.inorder(node.right)
    def postorder(self, node):
        if node.left is not None:
            node.postorder(node.left)
        if node.right is not None:
            node.postorder(node.right)
        print(node.x, node.y)

def solution(nodes):
    nodes.sort(key=lambda x: (-x[1], x[0]))
    node1 = Node(8, 6)
    for i in range(0, len(nodes)):
        x, y = nodes[i]
        n = Node(x, y)
        node1.insert(n)
    # node2 = Node(8, 6)
    # node1.insert(node2)
    node1.preorder(node1)
    print()
    node1.inorder(node1)
    print()
    node1.postorder(node1)


solution([[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3],  [7, 2], [2, 2]])
#[8, 6],