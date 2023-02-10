# 3시 23분 50분
# 실1
n = int(input())
dp = [[1] * 10 for _ in range(n+1)]
mod = 10_007
for i in range(1, n+1):
    num = dp[i-1][0]
    for j in range(1, 10):
        dp[i][j] = (num + dp[i-1][j]) % mod
        num += dp[i-1][j]

print(dp[n][-1])
