# 20시 40분 21시 17분
# 실1

n = int(input())
map1 = [ list(map(int, list(input()))) for _ in range(n)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
type = 0
answer = []
maxi = 0
def dfs(x, y):
    global maxi, map1
    map1[x][y] = 0
    for xx, yy in move:
        nx = xx + x
        ny = yy + y
        if 0 <= nx < n and 0 <= ny < n and map1[nx][ny] == 1:
            maxi += 1
            dfs(nx, ny)


for i in range(len(map1)):
    for j in range(len(map1[i])):
        maxi = 0
        if map1[i][j] == 1:
            map1[i][j] = 1
            type += 1
            maxi = 1
            dfs(i, j)
            answer.append(maxi)
answer.sort()
print(type)
for i in answer:
    print(i)
