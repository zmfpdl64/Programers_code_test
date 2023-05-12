# 21시 14분 21시 44분
# 실1

tree = {}
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
def pre_order(node):
    print(node.data, end=' ')
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=' ')
    if node.right_node != None:
        in_order(tree[node.right_node])
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=' ')
def solution(input):
    for i in input:
        cur, left, right = i
        tree[cur] = Node(cur, left, right)
    # 전위
    print('[ ',end='')
    pre_order(tree[1])
    print(']')

    # 중위
    print('[ ', end='')
    in_order(tree[1])
    print(']')

    # 후위
    print('[ ', end='')
    post_order(tree[1])
    print(']')

solution([[1,2,3], [2,4,5], [3,6,7], [4,None, None], [5, None, None], [6, None, None], [7, None, None]])