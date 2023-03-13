# 21시 20분 21시 30분
# 실2
import sys
sys.setrecursionlimit(10**5)
move = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
def dfs(x, y):
    a[x][y] = 0
    for xx, yy in move:
        nx = xx + x
        ny = yy + y
        if 0 <= nx < h and 0 <= ny < w and a[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int ,input().split())
    if w == 0 and h == 0:
        break;
    a = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 1:
                count += 1
                dfs(i, j)
    print(count)


