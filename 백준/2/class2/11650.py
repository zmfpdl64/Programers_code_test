#14시 14분 14시 19분

import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

a = list(sorted(a, key=lambda x: (x[0],x[1])))
for i in range(len(a)):
    print(' '.join(list(map(str, a[i]))))
