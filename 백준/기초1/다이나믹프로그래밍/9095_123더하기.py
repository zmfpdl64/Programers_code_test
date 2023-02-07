#4시 27분 4시 49분 22분
# 실3
n = int(input())
a = [int(input()) for _ in range(n)]
maxi = max(a)
dp = [0] * (maxi+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxi+1):
    dp[i] = dp[i-1]
    dp[i] += dp[i-2]
    dp[i] += dp[i-3]
for i in a:
    print(dp[i])

