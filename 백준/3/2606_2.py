
n = int(input())
m = int(input())

a = []
b = [[] for i in range(n+1)]
count = 0
vi_map = [False] * (n+1)
for i in range(m):
    x, y = map(int, input().split())
    a.append([x, y])

    b[x].append(y)
    b[y].append(x)
def dfs(s):
    global b, vi_map
    for i in b[s]:
        if vi_map[i] == False:
            vi_map[i] = True
            dfs(i)
    return
if m >= 1:
    dfs(a[0][0])
for i in vi_map:
    if i == True:
        count += 1
if count == 0:
    print(0)
else:
    print(count-1)
# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]
# for _ in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
#     graph[b].append(a)
    
# cnt = 0
# visited = [0]*(n+1)
# def dfs(start):
#     global cnt
#     visited[start] = 1
#     for i in graph[start]:
#         if visited[i]==0:
#             dfs(i)
#             cnt +=1
 
# dfs(1)
# print(cnt)