# 17시 45분 17시 57분
# 실1
from collections import deque
n = int(input())
move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,-2],[1,2],[-1,2],[-1,-2]]
for i in range(n):
    m = int(input())
    sx, sy = map(int ,input().split())
    ex, ey = map(int, input().split())
    vi_map = [[0 for _ in range(m)] for j in range(m)]
    vi_map[sx][sy] = 1
    q = deque([[sx,sy,0]])
    while q:
        x, y, cnt = q.popleft()
        if x == ex and y == ey:
            print(cnt)
            break;
        for xx, yy in move:
            nx = xx + x
            ny = yy + y
            if 0 <= nx < m and 0 <= ny < m and vi_map[nx][ny] == 0:
                vi_map[nx][ny] = 1
                q.append([nx,ny,cnt+1])

