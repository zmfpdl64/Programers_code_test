# 15시 38분
# LV 3
from collections import deque as d


def solution(rectangle, startX, startY, itemX, itemY):
    answer = 0
    vi_map = [[0] * 20 for _ in range(20)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for x1, y1, x2, y2 in rectangle:
        for i in range(y1 + 1, y2):
            vi_map[x1][i] += 1
            vi_map[x2][i] += 1
        for i in range(x1, x2 + 1):
            vi_map[i][y1] += 1
            vi_map[i][y2] += 1
    for i in vi_map:
        print(i)
    q = d([[startX, startY, 0, False]])
    # if vi_map[startX][startY] >= 2:
    # q.append([startX, startY, 0, True])
    # else:
    # q.append([[startX, startY,0, False]])

    while q:
        x, y, count, corner = q.popleft()
        if x == itemX and y == itemY:
            return count
        for nx, ny in move:
            xx = nx + x
            yy = ny + y
            if 0 < xx <= 50 and 0 < yy <= 50 and vi_map[xx][yy] >= 1:
                if corner == True:
                    if vi_map[xx][yy] == 1:
                        vi_map[xx][yy] = 0
                        q.append([xx, yy, count + 1, False])
                else:
                    if vi_map[xx][yy] == 1:
                        vi_map[xx][yy] = 0
                        q.append([xx, yy, count + 1, False])
                    elif vi_map[xx][yy] >= 2:
                        vi_map[xx][yy] = 0
                        q.append([xx, yy, count + 1, True])