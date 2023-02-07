#12시38분 12시 50분
# 실버4
import sys
input = sys.stdin.readline
n = int(input())

stack = []
for i in range(n):
    com = list(input().split())
    try:
        if len(com) == 1:
            cm = com[0]
            if cm == 'top':
                print(stack[-1])
            elif cm == 'pop':
                print(stack.pop())
            elif cm == 'empty':
                if len(stack) == 0:
                    print(1)
                else:
                    print(0)
            elif cm == 'size':
                print(len(stack))
        else:
            stack.append(com[1])
    except:
        print(-1)

