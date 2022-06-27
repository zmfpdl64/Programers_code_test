#14시 30분 14시 50분

import sys

a = list(map(int, sys.stdin.readline().split()))

b = [i for i in range(1, a[0]+1)]
answer = []
i = a[1]-1
while len(b) > 0:
    answer.append(b.pop(i))
    if len(b) == 0: break
    i = (i + a[1]-1) % len(b)
c = '<' + ', '.join(list(map(str,answer))) + '>'
print(c)