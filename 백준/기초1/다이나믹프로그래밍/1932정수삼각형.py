#4시 10분 4시 30분
# 실1
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = a[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + a[i][0]
    dp[i][len(a[i])-1] = dp[i-1][len(a[i-1])-1] + a[i][len(a[i])-1]
    for j in range(1, len(a[i])-1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]
print(max(dp[n-1]))