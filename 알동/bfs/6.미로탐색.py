# 2시 20분 38분
# 실1
# https://www.acmicpc.net/problem/2178
from collections import deque as d
import heapq
n, m = map(int, input().split())
maps = [list(map(int,list(input()))) for _ in range(n)]
move = [[0,1], [0,-1],[1,0],[-1,0]]
vi_map = [[False] * m for i in range(n)]
def bfs(x, y):
    queue = [[1, x, y]]
    vi_map[x][y] = True
    while queue:
        t, x, y = heapq.heappop(queue)
        if x == n-1 and y == m-1:
            return t
        for mx, my in move:
            nx = mx + x
            ny = my + y
            if 0 <= nx < n and 0 <= ny < m and not vi_map[nx][ny] and maps[nx][ny] == 1:
                vi_map[nx][ny] = True
                heapq.heappush(queue, [t+1, nx, ny])
print(bfs(0, 0))