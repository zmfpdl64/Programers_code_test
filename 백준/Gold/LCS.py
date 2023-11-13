# 15시 04분 15시 45분
# 골5
# https://www.acmicpc.net/problem/9251
str2 = "0ACCABCBAB"
str1 = "0CBBBAB"
# str1 = [0]+list(input().rstrip())
# str2 = [0]+list(input().rstrip())
n1, n2 = len(str1), len(str2)
dp = [[0] * n2 for i in range(n1)]
ans = 0
for i in range(1, n1):
    s1 = str1[i]
    for j in range(1, n2):
        s2 = str2[j]
        if s1 == s2:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(ans)
for i in dp:
    print(i)