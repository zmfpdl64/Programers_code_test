# 2시 2분 2시 30분
# 실1
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a = [[0,0,0]] + a
dp = [[0,0,0] for _ in range(n+1)]
for i in range(1, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) +a[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) +a[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) +a[i][2]
print(min(dp[n]))

