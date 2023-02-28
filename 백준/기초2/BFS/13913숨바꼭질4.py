# 16시 38분 17시 29분
# 골4
from collections import deque as d
n, m = map(int, input().split())
def bfs():
    q = d([[n,0]])
    vi_map = [[False, -1] for _ in range(100_001)]
    vi_map[n] = [True, -1]
    while q:
        pos, time = q.popleft()
        if pos == m:
            print(time)
            answer = []
            answer.append(pos)
            while time != 0:
                time -=1
                pos = vi_map[pos][1]
                answer.append(pos)
            return answer[::-1]

        move = [pos + 1, pos - 1, pos*2]
        for i in move:
            if 0 <= i <= 100_000 and not vi_map[i][0]:
                vi_map[i] = [True, pos]
                q.append([i, time+1])
print(*bfs())