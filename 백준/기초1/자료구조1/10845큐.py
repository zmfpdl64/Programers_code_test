#6시 25분 6시33분
# 실4
import sys
from collections import deque as de
input = sys.stdin.readline
n = int(input())
q = de()
for i in range(n):
    com = list(input().split())
    if len(com) == 2:
        cm = com[0]
        va = com[1]
        if cm == 'push':
            q.append(va)
    else:
        try:
            cm = com[0]
            if cm == 'pop':
                print(q.popleft())
            elif cm == 'size':
                print(len(q))
            elif cm == 'empty':
                if len(q) == 0:
                    print(1)
                else:
                    print(0)
            elif cm == 'front':
                num = q.popleft()
                print(num)
                q.appendleft(num)
            elif cm == 'back':
                num = q.pop()
                print(num)
                q.append(num)
        except:
            print(-1)

