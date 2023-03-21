# 20시 43분 21시
# 실2

n, g = map(int, input().split())
a = list(map(int, input().split()))
count = 0
seq = []
def dfs(depth, value, idx):
    global count
    if value == g and seq:
        count += 1
    if depth == n:
        return
    for i in range(idx, len(a)):
        seq.append(a[i])
        dfs(depth+1, value+a[i], i+1)
        seq.pop()

dfs(0, 0, 0)
print(count)