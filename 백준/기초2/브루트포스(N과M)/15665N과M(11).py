# 20시 26분 20시 30분
# 실2

n, m = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()
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