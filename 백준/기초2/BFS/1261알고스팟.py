# 16시 25분 18시
# 골4
from collections import deque as d
m, n = map(int, input().split())
vi_map = [[False] * m for _ in range(n)]
move = [[0,1],[0,-1],[1,0],[-1,0]]
a = []
for i in range(n):
    a.append(list(map(int, list(input()))))
q = d([[0,0,0]])
vi_map[0][0] = True
while q:
    x, y, ct = q.popleft()
    if x == n-1 and y == m-1:
        print(ct)
        exit()
    for mx, my in move:
        xx = x+mx
        yy = y+my
        if 0 <= xx < n and 0 <= yy < m and vi_map[xx][yy] == False:
            vi_map[xx][yy] = True
            p = a[xx][yy]
            if p == 0:
                q.appendleft([xx,yy,ct])
            else:
                q.append([xx,yy,ct+1])



