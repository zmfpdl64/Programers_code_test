# 19시 20분 19시 24분
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
        if a[i] not in answer:
            answer.append(a[i])
            dfs(i, depth+1)
            answer.pop()
dfs(0, 0)