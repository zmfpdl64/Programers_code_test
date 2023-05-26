import sys

input = sys.stdin.readline
n = int(input())
net = 0
answer = []
maps = []
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
vi_map = [[True] * n for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, input().split())))


def dfs(x, y, count):
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and vi_map[nx][ny] and maps[nx][ny] == 1:
            count += 1
            vi_map[nx][ny] = False
            count += dfs(nx, ny, count)
    return count


for i in range(n):
    for j in range(n):
        if vi_map[i][j] and maps[i][j] == 1:
            net += 1
            vi_map[i][j] = False
            answer.append(dfs(i, j, 1))

print(net)
print(answer)