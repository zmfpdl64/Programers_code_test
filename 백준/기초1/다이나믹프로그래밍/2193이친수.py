#11시12분 11시20분
n = int(input())
dp = [[0] * 2 for i in range(91)]
dp[1] = [0, 1]
dp[2] = [1, 0]
dp[3] = [1, 1]
for i in range(4, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(sum(dp[n]))