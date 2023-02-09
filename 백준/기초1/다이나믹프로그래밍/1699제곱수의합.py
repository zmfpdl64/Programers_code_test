#5시 50분 6시 28분
# 실2
n = int(input())
dp = [0] * 100_001
for i in range(1, n+1):
    dp[i] = i
    for j in range(1, i):
        if j ** 2 > i:
            break
        dp[i] = min(dp[i-j**2]+1, dp[i])
print(dp[n])