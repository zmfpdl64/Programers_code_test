# 12시 28분 12시 59분
# 실3

n = int(input())
dp = [1, 1, 2]
dp2 = [1, 1, 2]
for i in range(3, n):
    dp.append((dp[i-1]+dp[i-2]) %10007)
    dp2.append((dp2[i-1]+dp2[i-2]))
print(dp)
print(dp2)
print(dp[-1], dp2[-1]%10007)
