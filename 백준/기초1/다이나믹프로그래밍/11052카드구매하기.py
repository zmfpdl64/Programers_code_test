# 4시 53분
# 실1
n = int(input())
ins = list(map(int, input().split()))
dp = [0] + ins
for i in range(2, n+1):
    for j in range(len(ins)):
        if i - j >= 1 :
            dp[i] = max(dp[i], dp[i-j-1] + ins[j])
print(dp[n])

