# 2시 30분
# 실1

n = int(input())
dp = [[0,0] for _ in range(n+1)]
mod = 9_901
dp[1] = [2, 1]
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][1] *2 + dp[i-1][0])%mod
    dp[i][1] = sum(dp[i-1])%mod
print(sum(dp[n])% mod)
