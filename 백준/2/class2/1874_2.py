import sys
from collections import deque

n = int(input())
a = deque()
stack = deque()
answer = []
count = 0
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

while len(a) != 0:
    if len(stack) == 0 or stack[-1] != a[0]:
        count += 1
        stack.append(count)
        answer.append("+")
    else:
        a.popleft()
        answer.append("-")
        stack.pop()
    if n < count:
        answer.clear()
        break
if len(answer) != 2*n:
    print("NO")
else:
    for i in answer:
        print(i)

