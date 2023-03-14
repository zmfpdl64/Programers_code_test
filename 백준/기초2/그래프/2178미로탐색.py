# 20시 18분 20시 27분
# 실1
from collections import deque as d
import sys
input = sys.stdin.readline
h, w = map(int, input().split())
vi_map = [list(map(int, list(input().rstrip()))) for _ in range(h)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
vi_map[0][0] = 0
q = d([[0,0,1]])
while q:
    x, y, t = q.popleft()
    if x == (h-1) and y == (w-1):
        print(t)
        break;
    for xx, yy in move:
        nx = xx + x
        ny = yy + y
        if 0 <= nx < h and 0 <= ny < w and vi_map[nx][ny] == 1:
            vi_map[nx][ny] = 0
            q.append([nx,ny,t+1])
