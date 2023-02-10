# 5시 36분 6시 26분
# 실1

n = int(input())
a = [0] + [int(input()) for _ in range(n)]
dp =[[0,0,0] for _ in range(n+1)]
dp[1] = [0, a[1], 0]
for i in range(1, len(a)):
    dp[i][0] = dp[i-1][1] + a[i]
    dp[i][1] = dp[i-1][2] + a[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
print(max(dp[n]))