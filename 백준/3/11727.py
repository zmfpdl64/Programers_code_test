#13시 55분 
#1초 256MB 1<= N <= 1000

n=int(input())
dp = [i for i in range(n+2)]
dp[1] = 1
dp[2] = 3
for i in range(3, n+2):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n])