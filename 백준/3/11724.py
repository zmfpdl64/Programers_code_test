#21시 28분
#3초 512MB 1<= n <= 1000  1 <= m <= n*(n-1)/2
from     collections import deque as d
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[] for i in range(n+1)]
vi_map = [False] + [True for i in range(n)]
count = 0
q = d()
for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

for i in range(1, n+1):
    if vi_map[i] == True:
        vi_map[i] = False
        count += 1
        q.append(i)
        while q:
            pop = q.popleft()
            for j in a[pop]:
                if vi_map[j] == True:
                    vi_map[j] = False
                    q.append(j)
print(count)