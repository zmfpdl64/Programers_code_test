# 19시 57부
# 나머지합
# https://www.acmicpc.net/problem/10986
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
dp = [0] * n
dp[0] = a[0]%m
dp2 = [0] * 1_000_001
answer = 0
for i in range(1, len(a)):
    dp[i] = (dp[i-1] + a[i]) % m
    if dp[i] not in dic:
        dic[dp[i]] = 1
    else:
        dic[dp[i]] += 1

for i in range(1, 1_000_001):
    dp2[i] = dp2[i-1] + i
for i in dic.values():
    answer += dp2[i]
print(answer)


