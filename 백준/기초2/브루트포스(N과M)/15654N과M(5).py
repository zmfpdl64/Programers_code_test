# 19시 15분 19시 19분
# 실3
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
answer = []
def dfs(depth):
    if depth==m:
        print(*answer)
        return
    for i in a:
        if i not in answer:
            answer.append(i)
            dfs(depth+1)
            answer.pop()
dfs(0)
