# 16시 57분 17시 7분
# 실3
n = int(input())
a = [int(input()) for _ in range(n)]
maxi = max(a)
dp = [0] * (maxi+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, maxi+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
for i in a:
    print(dp[i])