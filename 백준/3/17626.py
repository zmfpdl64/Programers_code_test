#15시 07분
# 0.5초 512MB 1 <= n <= 50,000
# https://chanhuiseok.github.io/posts/baek-10/
# https://lakelouise.tistory.com/61
n = int(input())
count = 0
answer = []
dp = [i for i in range(n+1)]
dp[1] = 1
for i in range(1, n+1):
    for j in range(1, i):
        if i < j*j:
            break
        if dp[i] > dp[i - j*j] + 1:
            dp[i] = dp[i -j * j] + 1
print(dp[n])