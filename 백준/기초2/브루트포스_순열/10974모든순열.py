# 21시 05분 21시 7분
# 실3

n = int(input())
a = [i for i in range(1, n+1)]
answer = []
def dfs(depth):
    if depth == n:
        print(*answer)
        return
    for i in a:
        if i not in answer:
            answer.append(i)
            dfs(depth+1)
            answer.pop()
dfs(0)
