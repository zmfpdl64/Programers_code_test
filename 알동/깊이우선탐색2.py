# 19시 23분
# 실2
# https://www.acmicpc.net/problem/24480
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


n, m, r = map(int, input().rstrip().split())

# 1 : [2, 5]
# 2 : [1, 3, 5]
# 3 : [2]
# 4 : [7]
# 5 : [1, 2, 6]
# 6 : [5]
# 7 : [4]

count = 1
graph = [[] for i in range(n + 1)]
vi_map = [0 for i in range(n + 1)]

for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1):
    graph[i].sort(reverse=True)

# 1 : [4, 2]
# 2 : [1, 3, 4]
# 3 : [2, 4]
# 4 : [1, 2, 3]

# [1, 4, 2, 3]






def dfs(x):
    global vi_map, count
    vi_map[x] = count
    for i in graph[x]:
        if vi_map[i] == 0:
            count += 1
            vi_map[i] = count
            dfs(i)
# 1 : [4, 2]
# 2 : [4, 3, 1]
# 3 : [4, 2]
# 4 : [3, 2, 1]
# 5 : []

# [1, 4, 3, 2]

# vi_map = [1, 4, 3, 2, 0]

dfs(r)
for i in range(1, n+1):
    print(vi_map[i])