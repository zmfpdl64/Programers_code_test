# 20시 04분
# 20시 34분
import sys
from collections import deque
input = sys.stdin.readline
n  = int(input())
stack = deque()
for i in range(n):
    inp = input().rstrip().split(" ")
    if len(inp) == 2:
        stack.append(inp[1])
    else:
        ins = inp[0]
        if ins == "front":
            if stack:
                print(stack[0])
            else:
                print(-1)
        elif ins == "back":
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif ins == "empty":
            if stack:
                print(0)
            else:
                print(1)
        elif ins == "pop":
            if stack:
                print(stack.popleft())
            else:
                print(-1)
        elif ins == "size":
            print(len(stack))

