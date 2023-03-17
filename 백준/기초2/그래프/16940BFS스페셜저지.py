#18시 21분
# 골3
from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
vi_map = [0] * (n+1)
q = deque([])
for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
seq = list(map(int, input().split()))
for i in graph[1]:
    q.append([i,2])
vi_map[1] = 1
while q:
    nex, cnt = q.popleft()
    vi_map[nex] = cnt
    for i in graph[nex]:
        if vi_map[i] == 0:
            q.append([i,cnt+1])
answer = 1
for i in range(len(seq)-1):
    if (vi_map[seq[i+1]]-vi_map[seq[i]]) >= 0:
        pass
    else:
        answer = 0
        break
print(answer)

