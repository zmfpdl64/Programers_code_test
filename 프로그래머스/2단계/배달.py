# 20시 10분
# 20시 36분 26분
# https://school.programmers.co.kr/learn/courses/30/lessons/12978

import heapq


def solution(N, road, K):
    answer = 0
    graph = {i: [] for i in range(N + 1)}
    for i in road:
        a, b, c = i
        graph[a].append([b, c])
        graph[b].append([a, c])

    def bfs(graph):
        result = 0
        dest = [10_000_000 for _ in range(N + 1)]
        q = [[1, 0]]
        while q:
            des, t = heapq.heappop(q)
            if dest[des] > t:
                dest[des] = t
                for i in graph[des]:
                    nd, nt = i
                    heapq.heappush(q, [nd, t + nt])
        for i in range(1, len(dest)):
            if dest[i] <= K:
                result += 1
        return result

    return bfs(graph)