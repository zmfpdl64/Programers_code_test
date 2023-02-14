#6시 13분
# 골4
n = int(input()) // 2
dp = [0] * 16
dp[1] = 3
for i in range(2, n+1):
    dp[i] = dp[i-1] * 3 + sum(dp[:i-1]) * 2 + 2
