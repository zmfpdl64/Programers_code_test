#18시 3분  18시 16분
import sys
from collections import deque


stack = deque([i for i in range(1, int(sys.stdin.readline()) + 1 )])
while len(stack) != 1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack[0])