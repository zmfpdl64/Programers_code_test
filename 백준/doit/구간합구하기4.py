# 18시 27분 18시 27분
# 실3
# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ins = list(map(int,input().split()))
dp = [0] * (n)
dp[0] = ins[0]
for i in range(1, len(ins)):
    dp[i] = dp[i-1] + ins[i]
dp = [0] + dp
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])

