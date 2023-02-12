#4시 33분 4시 58분
# 실2
n = int(input())
a = list(map(int ,input().split()))
dp = a.copy()
for i in range(1, len(a)):
    for j in range(i):
        if a[i] > a[j] and dp[i] < a[i]+dp[j]:
            dp[i] = dp[j] + a[i]
print(max(dp))
