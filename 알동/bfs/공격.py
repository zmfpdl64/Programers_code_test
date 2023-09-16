import heapq
import sys
import math
input =sys.stdin.readline
n, r, d, x, y = map(int, input().split())
tower = []
total = 0
graph = { i : [] for i in range(n+1)}
vi_map = [False] * (n+1)
tower.append([x, y])
for i in range(n):
    tower.append(list(map(int, input().split())))
for i in range(len(tower)):
    # _x, _y = tower[i]
    # _dis = math.sqrt(abs(x - _x) ** 2 + abs(_y - y) ** 2)
    for j in range(i+1, len(tower)):
        x1, y1 = tower[i]
        x2, y2 = tower[j]
        dis = math.sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)
        if dis <= r:
            graph[i].append(j)
            graph[j].append(j)
            # heapq.heappush(graph[i], [dis, x2, y2])
            # heapq.heappush(graph[j], [dis, x1, y1])
def bfs():
    global total
    queue = [[0, 0]]
    vi_map[0] = True
    while queue:
        t, id = heapq.heappop(queue)
        for i in graph[id]:
            if not vi_map[i]:
                vi_map[i] = True
                total += d * (2 ** -t)
                heapq.heappush(queue, [t+1, i])
bfs()
print(f"{total:.2f}")