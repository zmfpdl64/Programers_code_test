# 20시 15분 20시 20분
# 실2

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = {}
answer = []
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
def dfs(depth, value):
    if depth == m:
        print(*answer)
        return
    for i in b.keys():
        if value <= i and b[i] != 0:
            b[i] -= 1
            answer.append(i)
            dfs(depth+1, i)
            answer.pop()
            b[i] += 1
dfs(0, 0)