# 15시 23분 16시 36분
# 실1
from collections import deque as d
n, m = map(int ,input().split())
def bfs():
    q = d([[n, 0]])
    vi_map = [False] * 100_001
    vi_map[n] = True
    while q:
        pos, time = q.popleft()
        if pos == m:
            return time
        move = [pos+1,pos-1,pos*2]
        for i in move:
            if 0 <= i <= 100_000 and vi_map[i] == False:
                vi_map[i] = True
                q.append([i, time+1])
print(bfs())

