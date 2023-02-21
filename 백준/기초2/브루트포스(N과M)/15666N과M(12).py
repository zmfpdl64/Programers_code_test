# 20시 33분 20시 35분
# 실2
n, m = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()
answer = []
def dfs(depth, idx):
    if depth == m:
        print( * answer)
        return
    for i in range(idx, len(a)):
        answer.append(a[i])
        dfs(depth+1, i)
        answer.pop()
dfs(0, 0)