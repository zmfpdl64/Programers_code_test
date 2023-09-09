# 15시 32분
# 골2
# https://www.acmicpc.net/problem/16946
import sys
import copy
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for i in range(n)]
result = []
move = [[0,1],[0, -1],[1,0],[-1,0]]
vi_map = [[False] * m for i in range(n)]

def dfs(x, y, count, vi_map):
    for mx, my in move:
        nx = x + mx
        ny = y + my
        if 0 <= nx < n and 0 <= ny < m and not vi_map[nx][ny] and maps[nx][ny] == 0:
            vi_map[nx][ny] = True
            count = max(dfs(nx, ny, count+1, vi_map), count)

def bfs(x, y, count, vi_map):
    queue = []
    queue.append()
# n^2 * m^2 -> n * m
for i in range(len(maps)):
    line = []
    for j in range(len(maps[i])):
        if maps[i][j] == 1:
            maps[i][j] = 0
            count = dfs(i, j, 0, copy.deepcopy(vi_map))
            maps[i][j] = 1
            line.append(count)
        else:
            line.append(0)
    result.append(line)
for i in result:
    print(''.join(map(str, i)))
