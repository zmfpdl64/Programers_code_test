# 19시 04분
# 골4
from collections import deque as d
n = int(input())
for i in range(n):
    e, v = map(int, input().split())
    a = [[] for _ in range(e+1)]
    vi_map = [0 for _ in range(e+1)]
    q = d();
    for i in range(v):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)

    count = 0
    def dfs(idx):
        global vi_map, count
        if len(a[idx]) == 0:
            return
        for i, v in enumerate(a[idx]):
            if vi_map[v] == 0:
                vi_map[v] = 1
                dfs(v)

    for i in range(1, len(a)):
        if vi_map[i] == 0:
            print(vi_map)
            print(a)
            vi_map[i] = 1
            dfs(i)
            count += 1
            print(vi_map)
    print(count)






