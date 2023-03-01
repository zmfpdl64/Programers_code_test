# 10시 47분 11시 59분
# 골4
from collections import deque as d
def solution():
    n = int(input())
    q = d([[1,0,0]])
    vi_map = [[False] * 1_001 for _ in range(1_001)]
    vi_map[1][0] = True
    while q:
        count, copy, time = q.popleft()
        if count == n:
            return time
        act = [[count, count, time+1], [count + copy, copy, time+1], [count-1, copy, time+1]]
        for ct, cy, ti in act:
            if 0<= ct <= 1000 and not vi_map[ct][cy]:
                q.append([ct,cy,ti])
                vi_map[ct][cy] = True
print(solution())