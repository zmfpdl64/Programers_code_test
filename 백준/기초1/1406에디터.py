#4시 06분
# 실2
import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
n = int(input())
idx = len(left)
for i in range(n):
    com = list(input().split())
    if len(com) == 2:
        if com[0] == 'P':
            st = com[1]
            left.append(st)
    else:
        cm = com[0]
        if cm == 'L' and len(left) != 0:
            right.append(left.pop())
        elif cm == 'D' and 0 != len(right):
            left.append(right.pop())
        elif cm == 'B' and len(left) != 0:
            left.pop()
print("".join(left) + "".join(right)[::-1])
