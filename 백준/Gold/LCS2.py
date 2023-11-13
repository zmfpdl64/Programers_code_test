# 17시 16분
# 골4
# https://www.acmicpc.net/problem/9252

str1 = [0] + list(input().rstrip())
str2 = [0] + list(input().rstrip())
n1 = len(str1)
n2 = len(str2)
dp = [[0]*n2 for _ in range(n1)]
ans = []
maxi = 0
for i in range(1, n1):
    s1 = str1[i]
    for j in range(1, n2):
        s2 = str2[j]
        if s1==s2:
            dp[i][j] = dp[i-1][j-1] + 1
            maxi = max(maxi, dp[i][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
cur_idx = maxi
move = [[-1, 0], [0, -1], [-1, -1]]
x, y = n1, n2
while len(ans) != maxi:
    for mx, my in move:
        nx = mx + x
        ny = my + y
        if 0 <= nx < n1 and 0 <= ny < n2 and cur_idx == dp[nx][ny]:
            x = nx
            y = ny
            cur_idx -= 1
            ans.append(str2[nx])
            break
    else:
        x -= 1
print(maxi)
print(''.join(ans))

