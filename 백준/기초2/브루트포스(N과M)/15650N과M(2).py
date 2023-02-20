# 17시 38분 17시 45분
# 실3
n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
answer = []
def dfs(index, depth):
    if depth == m:
        print(*answer)
        return
    for i in range(index, n):
        answer.append(a[i])
        dfs(index+1, depth+1)
        answer.pop()
dfs(0, 0)
