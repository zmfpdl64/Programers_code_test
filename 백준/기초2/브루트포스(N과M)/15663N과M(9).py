# 19시 47분 20시 07분
# 실2

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
answer = []
def dfs(depth):
    if depth == m:
        print(*answer)
        return
    for i in b.keys():
        if b[i] > 0:
            b[i] -= 1
            answer.append(i)
            dfs(depth+1)
            b[i] += 1
            answer.pop()
dfs(0)
