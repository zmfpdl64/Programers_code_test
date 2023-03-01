# 골5
from collections import deque
def solution():
    n, m = map(int, input().split())
    q = deque([[n, 0]])
    vi_map = [False] * 100_001
    vi_map[n] = True
    while q:
        start, time = q.popleft()
        if start == m:
            return time
        move = [2*start, start-1, start+1]
        for i in move:
            if 0<= i <= 100_000 and not vi_map[i]:
                if i == 2*start:
                    q.appendleft([i, time])
                else:
                    q.append([i, time+1])
                vi_map[i] = True
print(solution())