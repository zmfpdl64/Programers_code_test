from collections import deque
def dfs(x):
    global a, vi_map, answer
    if vi_map[x] == True:
        vi_map[x] = False
        answer.append(x)

    for i in a[x]:
        if vi_map[i] == True:
            vi_map[i] = False
            answer.append(i)
            dfs(i)

n, m, v = map(int, input().split())
vi_map = [False] + [True for _ in range(n)]
vi_map2 = [False] + [True for _ in range(n)]
a = [[] for _ in range(n+1)]
answer = []
answer2 = []
q = deque()
for i in range(m):
    r, c = map(int, input().split())
    a[r].append(c)
    a[c].append(r)
if a[v] != []:
    for i in range(len(a)):
        a[i].sort()
    answer.append(v)
    q.append(v)
    vi_map[v] = False
    vi_map2[v] = False

    for i in a[v]:
        dfs(i)
    for i, va in enumerate(a):
        if vi_map[i] == True:
            vi_map[i] = False
            dfs(i)
        for j in va:
            if vi_map[j] == True:
                vi_map[j] = False
                dfs(j)

    while q:
        po = q.popleft()
        answer2.append(po)
        for i in a[po]:
            if vi_map2[i] == True:
                vi_map2[i] = False
                q.append(i)
    print(answer)
    print(answer2)
else:
    print(v)
    print(v)