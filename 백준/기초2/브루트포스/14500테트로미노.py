#20시 08분 21시 33분
# 골4

def dfs(x, y, depth, value):
    global maxi
    if depth == 4:
        maxi = max(maxi, value)
        return
    if depth == 2:
        for i in range(len(move)-1):
            x1, y1 = move[i]
            try:
                if vi_map[x + x1][y + y1] == False and x+x1 >= 0 and y+y1 >= 0:
                    vi_map[x+x1][y+y1] = True
                    value += a[x+x1][y+y1]
                    for j in range(len(move)):
                        x2, y2 = move[j]
                        try:
                            if vi_map[x + x2][y + y2] == False and x+x2 >= 0 and y+y2 >= 0:
                                vi_map[x+x2][y+y2] = True
                                value += a[x+x2][y+y2]
                                maxi = max(maxi, value)
                                vi_map[x+x2][y+y2] = False
                                value -= a[x+x2][y+y2]
                        except:
                            pass
                    vi_map[x+x1][y+y1] = False
                    value -= a[x+x1][y+y1]
            except:
                pass
    for x1, y1 in move:
        mox, moy = x+x1, y+y1
        try:
            if vi_map[mox][moy] == False and mox >= 0 and moy >= 0:
                vi_map[mox][moy] = True
                value += a[mox][moy]
                dfs(mox, moy, depth+1, value)
                value -= a[mox][moy]
                vi_map[mox][moy] = False
        except IndexError:
            pass
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
maxi = 0
vi_map = []
for i in range(n):
    vi_map.append([False for _ in range(m)])
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
for i in range(len(a)):
    for j in range(len(a[i])):
        vi_map[i][j] = True
        dfs(i, j, 1, a[i][j])
        vi_map[i][j] = False
print(maxi)
