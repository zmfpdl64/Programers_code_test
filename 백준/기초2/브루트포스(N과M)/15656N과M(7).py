# 19시 35분 19시 42분
# 실3
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = []
def dfs(depth):
    if depth == m:
        print(*answer)
        return
    for i in range(n):
        answer.append(a[i])
        dfs(depth+1)
        answer.pop()
dfs(0)