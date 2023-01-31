import sys

input = sys.stdin.readline

n = int(input())
ans = float("inf")
data = [list(map(int, input().split())) for _ in range(n)]


def total(team):
    res = 0
    for a in team:
        for b in team:
            res += data[a][b]
    return res


def dfs(start, team):
    global ans

    if len(team) == n // 2:
        other = [i for i in range(n) if i not in team]
        ans = min(abs(total(team) - total(other)), ans)
        return
    for i in range(start, n):
        dfs(i + 1, team + [i])


dfs(0, [])
print(ans)