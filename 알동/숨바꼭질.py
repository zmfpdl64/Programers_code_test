# 0시 14분
# 실 1
# https://www.acmicpc.net/problem/1697

# from collections import deque as d
# n, m = map(int ,input().split())
# def bfs():
#     q = d([[n, 0]])
#     vi_map = [False] * 100_001
#     vi_map[n] = True
#     while q:
#         pos, time = q.popleft()
#         if pos == m:
#             return time
#         move = [pos+1,pos-1,pos*2]
#         for i in move:
#             if 0 <= i <= 100_000 and vi_map[i] == False:
#                 vi_map[i] = True
#                 q.append([i, time+1])
# print(bfs())


import heapq
n, m = map(int, input().split())
queue = [[0, n]]
while queue:
    t, cur = heapq.heappop(queue)
    if cur == m:
        print(t)
        break
    move = [cur+1, cur-1, cur*2]
    for nex in move:
        if 0 <= nex <= 100_000:
            heapq.heappush(queue, [t+1, nex])

