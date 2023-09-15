# 23시 52분
# 실 2
# https://www.acmicpc.net/problem/4963
from collections import deque

move = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    maps =[]
    count = 0
    vi_map = [[False] * n for i in range(m)]
    for i in range(m):
        maps.append(list(map(int, input().split())))

    for i in range(m):
        for j in range(n):
            if not vi_map[i][j] and maps[i][j] == 1:
                vi_map[i][j] = True
                q = deque([[i, j]])
                count += 1
                while q:
                    x, y = q.popleft()
                    for mx, my in move:
                        nx = mx + x
                        ny = my + y
                        if 0 <= nx < m and 0 <= ny < n and vi_map[nx][ny] == 0 and maps[nx][ny] == 1:
                            vi_map[nx][ny] = True
                            q.append([nx, ny])
    print(count)

