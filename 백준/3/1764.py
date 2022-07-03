#16시 06분 16tl 21분 클리어 사실 좀 더 빠르게 클리어 가능했음


#조건 2초 256MB  1<= M, N <= 500,000

import sys
input = sys.stdin.readline
dic = {}
n, m = map(int, input().split())
a = []
for i in range(n+m):
    name = input().rstrip()
    if name in dic:
        dic[name] = 1
        a.append(name)
    else:
        dic[name] = 0
print(len(a))
a.sort()
for i in a:
    print(i)



