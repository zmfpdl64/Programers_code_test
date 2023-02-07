#7시32분 7시38분
# 실4
import sys
from collections import deque as de
input = sys.stdin.readline
n = int(input())
a = de()
for i in range(n):
    com = list(input().split())
    if len(com) == 2:
        cm = com[0]
        va = com[1]
        if cm == 'push_front':
            a.appendleft(va)
        elif cm == 'push_back':
            a.append(va)
    else:
        cm = com[0]
        try:
            if cm == 'pop_front':
                print(a.popleft())
            elif cm == 'pop_back':
                print(a.pop())
            elif cm == 'size':
                print(len(a))
            elif cm == 'empty':
                if len(a) == 0:
                    print(1)
                else:
                    print(0)
            elif cm == 'front':
                num = a.popleft()
                print(num)
                a.appendleft(num)
            elif cm == 'back':
                num = a.pop()
                print(num)
                a.append(num)
        except:
            print(-1)
