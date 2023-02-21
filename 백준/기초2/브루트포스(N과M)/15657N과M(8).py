# 19시 44분 19시 47분
# 실3

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = []
def dfs(idx, depth):
    if depth == m:
        print(*answer)
        return
    for i in range(idx, n):
        answer.append(a[i])
        dfs(i, depth+1)
        answer.pop()
dfs(0, 0)