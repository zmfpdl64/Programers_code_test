# 1시 1시 8분
# 실3

dp = [0, 1, 3]
n = int(input())
for i in range(3, n+1):
    dp.append((dp[i-1]+dp[i-2]*2) % 10007)
print(dp[n])
ㅊ퓨ㅜ