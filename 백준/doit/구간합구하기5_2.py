# 19시 22분
# 실 1
# https://www.acmicpc.net/problem/11660

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
ins = []
for i in range(m):
    ins.append(list(map(int,input().split())))
dp = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + maps[i-1][j-1]
for i in ins:
    x1, y1, x2, y2 = i
    num = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(num)
