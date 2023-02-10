# 1시 53분 2시
# 실2
n = int(input())
a = [int(input()) for _ in range(n)]
maxi = max(a)
mod = 1_000_000_009
dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxi+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%mod
for i in a:
    print(dp[i])

