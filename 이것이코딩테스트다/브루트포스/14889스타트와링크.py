import sys
def dfs(depth, idx):
    global graph, vi_map, min_value,n
    if depth == n//2:
        asum = 0
        bsum = 0
        for i in range(n):
            for j in range(n):
                if vi_map[i] and vi_map[j]:
                    asum += graph[i][j]
                elif not vi_map[i] and not vi_map[j]:
                    bsum += graph[i][j]
        min_value = min(min_value, abs(asum - bsum))
        return
    for i in range(idx, n):
        if not vi_map[i]:
            vi_map[i] = True
            dfs(depth+1, i+1)
            vi_map[i] = False
f = open('startexample.txt', 'r')
input = f.readline
for _ in range(2):
    n = int(input())
    vi_map = [False] * n
    graph = [list(map(int, input().split())) for _ in range(n)]
    min_value = sys.maxsize
    dfs(0, 0)
    print(min_value)