import heapq
from collections import deque
n, m = map(int, input().split())

queue = deque([])
vi_map = [[-1, -1] for i in range(500_001)]
queue.appendleft([0, n])
def calc(time):
    return time * (time+1) // 2
def chk(loc):
   return 0 <= loc <= 500_000
while queue:
    t, cur = queue.popleft()
    # if not chk(cur) or vi_map[cur][t%2] != -1:
    #     continue
    # if vi_map[cur][t%2] != -1:
    #     continue

    # vi_map[cur][t%2] = t

    # move = [cur + 1, cur - 1, cur * 2]
    # for i in move:
    #     queue.append([t+1, i])

    move = [cur + 1, cur - 1, cur * 2]
    for i in move:
        if chk(i) and (vi_map[i][(t+1) % 2] == -1):
            vi_map[i][(t+1) % 2] = t+1
            queue.append([t+1, i])

for i in range(500_001):
    next = m + (i * (i + 1)) // 2
    if next > 500_000:
        break
    if vi_map[next][i % 2] != -1 and vi_map[next][i % 2] <= i:
        print(i)
        exit()
print(-1)