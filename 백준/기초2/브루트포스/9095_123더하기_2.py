# 17시 12분 17시 18분

n = int(input())
a = [int(input()) for _ in range(n)]
maxi = max(a)
ad = [1,2,3]
count = 0
def dfs(value, goal):
    global count
    if value == goal:
        count += 1
        return
    elif value > goal:
        return
    for i in ad:
        dfs(value+i, goal)

for i in a:
    count = 0
    for j in ad:
        dfs(j, i)
    print(count)
