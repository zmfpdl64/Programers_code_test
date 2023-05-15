# 통과
import sys
sys.setrecursionlimit(10**6)
def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            o = computers[i][j]
            if o == 1:
                graph[i].append(j)
                graph[j].append(i)
    vi_map = [True] * n
    def dfs(graph, vi_map, x):
        for i in graph[x]:
            if vi_map[i]:
                vi_map[i] = False
                dfs(graph, vi_map, i)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if vi_map[graph[i][j]]:
                vi_map[graph[i][j]] = False
                dfs(graph, vi_map, graph[i][j])
                answer +=1
    return answer