# 20시 49분 22시 11분
# 골5
from collections import deque as d
import copy
w, h = map(int, input().split())
t_map = [list(map(int, input().split())) for _ in range(h)]
vi_map = copy.deepcopy(t_map)
move = [[0,1],[0,-1],[1,0],[-1,0]]
pos = []
one = 0
q = d([])
for i in range(len(t_map)):
    for j in range(len(t_map[i])):
        if t_map[i][j] == 1:
            one += 1
            q.append([i,j,0])
while q:
    x, y, t = q.popleft()
    for xx, yy in move:
        nx = xx + x
        ny = yy + y
        if 0 <= nx < h and 0 <= ny < w and vi_map[nx][ny] != -1 and vi_map[nx][ny] != 1:
            vi_map[nx][ny] == -1
            if t_map[nx][ny] == 0:
                t_map[nx][ny] = t+1
                q.append([nx,ny,t+1])
            else:
                if t_map[nx][ny] > (t+1):
                    t_map[nx][ny] = t+1
                    q.append([nx,ny,t+1])
mini = -1
count = 0
for i in t_map:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        elif j == -1:
            count +=1
    mini = max(mini, max(i))
if w*h - count == one:
    print(0)
else:
    print(mini)
