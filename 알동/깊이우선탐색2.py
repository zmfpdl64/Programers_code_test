# 19시 23분
# 실2
# https://www.acmicpc.net/problem/24480
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n, m, r = map(int, input().rstrip().split())
count = 1
graph = [[] for i in range(n + 1)]
vi_map = [0 for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1, n+1):
    graph[i].sort(reverse=True)
def dfs(x):
    global vi_map, count
    vi_map[x] = True
    vi_map[x] = count
    for i in graph[x]:
        if vi_map[i] == 0:
            count += 1
            vi_map[i] = count
            dfs(i)
dfs(r)
for i in range(1, n+1):
    print(vi_map[i])