# 23시 59분 0시 20분
# 실2
# https://www.acmicpc.net/problem/1260

# 단 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것부터 방문
# 정점의 갯수 1 <= N <= 1000
# 간선의 수 1 <= M <= 10,000
# 시간 복잡도  M(M-1) / 2  visit_map이 있다는 가정하에
# 시작 노드 V
# 간선은 양방향이다.

import sys
from collections import deque as d
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]
vi_map = [False] * (N+1)
ans1 = []
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 조건에 올림차순 
for i in range(len(graph)):
    graph[i].sort()

# 1 : [2, 3]
# 2 : [1, 5]
# 3 : [1, 4]
# 4 : [3, 5]
# 5 : [2, 4]
def dfs(s):
    global vi_map
    vi_map[s] = True
    ans1.append(s)
    for i in graph[s]:
        if vi_map[i] == 0:
            dfs(i)

_vi_map = [False] * (N+1)
_vi_map[V] = True
ans2 = []
ans2.append(V)

# 1 : [2, 3]
# 2 : [1, 5]
# 3 : [1, 4]
# 4 : [3, 5]
# 5 : [2, 4]
def bfs(s):
    global _vi_map
    queue = d([s])
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if _vi_map[i] == 0:
                ans2.append(i)
                _vi_map[i] = True
                queue.append(i)
dfs(V)
bfs(V)
print(*ans1)
print(*ans2)
