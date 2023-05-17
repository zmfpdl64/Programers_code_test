# 20시 40분
# 20시 50분 10분

import heapq
def solution(N, road, K):
    answer = 0
    graph = {i : [] for i in range(1, N+1)}
    for a, b, c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
    def bfs(graph):
        result = 0
        maps = [30_000_000 for _ in range(N+1)]
        q =[[1, 0]]
        while q:
            node, time = heapq.heappop(q)
            if time < maps[node]:
                maps[node] = time
                for n_node, n_time in graph[node]:
                    if n_time + time < maps[n_node]:
                        heapq.heappush(q, [n_node, time + n_time])
        for i in range(1, len(maps)):
            if maps[i] <= K:
                result +=1
        return result
    return bfs(graph)