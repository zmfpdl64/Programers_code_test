#1시 14분
# 실2
n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(len(a)):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))