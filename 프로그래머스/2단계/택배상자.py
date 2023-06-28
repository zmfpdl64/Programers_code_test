# 16시 45분
# 17시 29분 44분..
from collections import deque
def solution(order):
    answer = 1
    order = deque(order)
    stack = []
    result = []
    size = len(order)
    for i in range(1, size + 1):
        stack.append(i)

        while stack:
            if order and stack[-1] == order[0]:
                num = stack.pop()
                order.popleft()
                result.append(num)
            else:
                break
    return len(result)