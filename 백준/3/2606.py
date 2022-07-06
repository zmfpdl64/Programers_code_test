#11시 15분 바이러스 1시 57분
# 1초 128MB   1 <= n <= 100 네트워크에 포함된 컴퓨터 m
# dfs 탐색

import sys
def dfs(s, v):
    global vi_map
    for i in s[v]:
        if vi_map[i] == False:
            vi_map[i] = True
            dfs(s, i)

input = sys.stdin.readline
n = int(input())
a = []
b = [ [] for i in range(n+1)]
m = int(input())
global vi_map
vi_map = [False] * (n+1)
for i in range(m):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    x = a[i][0]
    y = a[i][1]
    b[x].append(y)
    b[y].append(x)
if len(a) != 0:
    dfs(b, a[0][0])

count = 0
for i, v in enumerate(vi_map):
    if i != a[0][0] and v == True:
        count += 1
if len(a) != 0:
    print(count)
else:
    print(0)
