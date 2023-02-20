# 18시
# 실3
n, m = map(int, input().split())
a = [i for i in range(1, n+1)]
answer = []
def dfs(depth):
    if depth == m:
        print(*answer)
        return
    for i in a:
        answer.append(i)
        dfs(depth+1)
        answer.pop()
dfs(0)