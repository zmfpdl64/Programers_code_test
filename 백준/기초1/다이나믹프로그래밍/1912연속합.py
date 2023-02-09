# 5시 27분 5시 48분
# 실2
n = int(input())
a = list(map(int, input().split()))
dp = [-1000] * 100_001
dp[0] = a[0]
for i in range(1, len(a)):
    if dp[i-1] < 0:
        dp[i] = a[i]
    else:
        dp[i] = dp[i-1] + a[i]
print(max(dp))
