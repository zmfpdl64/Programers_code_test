# 21시 42분
# 2초 128MB 1 <= n <= 1000  1 <= M <= 10,000

from collections import deque


n, m, v = map(int, input().split())
vi_map = [False] + [True for _ in range(n)]
vi_map2 = [False] + [True for _ in range(n)]

a = [[] for i in range(n+1)]
answer = []
queue = deque()
answer2 = []
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
def dfs(s):
    global vi_map, answer, a
    if vi_map[s] == True:
        answer.append(s)
        vi_map[s] = False
        for i in a[s]:
            dfs(i)
answer.append(v)
vi_map[v] = False
for i in a[v]:
    dfs(i)
for i, va in enumerate(a):
    if vi_map[i] == True:
        vi_map[i] = False
        answer.append(i)
    for j in va:
        dfs(j)


if vi_map2[v] == True:
    queue.append(v)
    vi_map2[v] = False
while queue:
    po = queue.popleft()
    answer2.append(po)
    for i in a[po]:
        if vi_map2[i] == True:
            queue.append(i)
            vi_map2[i] = False

        

                

print(answer)
print(answer2)
# for i in range(len(a)):
#     a[i].sort()
# answer.append(v)
# answer2.append(v)
# vi_map[v] = False
# vi_map2[v] = False
# for i in a[v]:
#     dfs(i)
# for i in a:
#     for j in i:
#         dfs(j)

# for i in a[v]:
#     if vi_map2[i] == True:
#         vi_map2[i] = False
#         answer2.append(i)

# for i in a:
#     for j in i:
#         if vi_map2[j] == True:
#             vi_map2[j] = False
#             answer2.append(j)
# print(' '.join(map(str,answer)))
# print(' '.join(map(str, answer2)))
