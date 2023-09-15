# 1시
# 실2
# https://www.acmicpc.net/problem/15270

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
vi_map = [False for i in range(n+1)]
ans_list = []
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(ans, idx):
    vi_map[idx] = True

    for i in range(len(graph)):
        if not vi_map[i]:
            vi_map[i] = True
            ans.append(i)
            dfs(ans, i)
            vi_map[i] = False



