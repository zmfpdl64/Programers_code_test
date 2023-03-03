# LV 3
from collections import deque as d
def solution(rectangle, startX, startY, itemX, itemY):
    answer = 0
    vi_map = [[0] * 102 for _ in range(102)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:  # 내부일 때
                    vi_map[i][j] = 0
                elif vi_map[i][j] != 0:  # 테두리일 때 그리고 이미 내부가 아닐 때
                    vi_map[i][j] = 1  # 테투리랑 내부랑 겹치면 그건 내부
    q = d([[startX, startY, 0]])
    while q:
        x, y, count = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return count//2
        for nx, ny in move:
            xx = nx + x
            yy = ny + y
            if 0 < xx <= 101 and 0 < yy <= 101 and vi_map[xx][yy] >= 1:
                vi_map[xx][yy] = 0
                q.append([xx,yy,count+1])
maps = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
cx, cy = 1, 3
itx, ity = 7, 8

print(solution(maps, cx, cy, itx, ity))