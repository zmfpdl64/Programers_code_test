# 23시 28분 23시 50분 22분
# 실버2
# https://www.acmicpc.net/problem/24444
from collections import deque as q
n, m, r = map(int,input().split())
gph = [[] for i in range(n+1)]
vi_map = [0] * (n+1)
count = 1
for i in range(m):
    u, v = map(int, input().split())
    gph[u].append(v)
    gph[v].append(u)
for i in range(len(gph)):
    gph[i].sort()
if not gph[r]:
    for i in range(n):
        print(0)
    exit()
queue = q([r])
vi_map[r] = count
while queue:
    nex = queue.popleft()
    for i in gph[nex]:
        if not vi_map[i]:
            count += 1
            vi_map[i] = count
            queue.append(i)
for i in range(1, len(vi_map)):
    print(vi_map[i])





