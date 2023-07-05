# 구간합 구하기5
# 19시 30분
# https://www.acmicpc.net/problem/11660
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
maps = []
for i in range(n):
    line = list(map(int,input().split()))
    maps.append(line)
dp = [[0] * (n+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + maps[i-1][j-1]
for i in range(m):
    x1,y1,x2,y2= map(int, input().split())
    num = dp[x2][y2] - dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    print(num)




