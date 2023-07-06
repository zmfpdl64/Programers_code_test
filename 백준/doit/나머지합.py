# 나머지합
# https://www.acmicpc.net/problem/10986
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
dic = {}
dp = [0] * n
dp[0] = a[0] % m
dic[dp[0]] = 1
answer = 0
for i in range(1, len(a)):
    dp[i] = (dp[i - 1] + a[i]) % m
    num = dp[i]
    if dp[i] not in dic:
        dic[dp[i]] = 1
    else:
        dic[dp[i]] += 1
for i in dic.values():
    answer += i * (i - 1) // 2
if 0 in dic:
    answer += dic[0]

print(answer)


# def solution(n, m, a):
#     dic = {}
#     dp = [0] * n
#     dp[0] = a[0]%m
#     dic[dp[0]] = 1
#     answer = 0
#     for i in range(1, len(a)):
#         dp[i] = (dp[i-1] + a[i]) % m
#         num = dp[i]
#         print(num)
#         if dp[i] not in dic:
#             dic[dp[i]] = 1
#         else:
#             dic[dp[i]] += 1
#     for i in dic.values():
#         answer += i*(i-1)//2
#     print(answer)
#
# solution(6, 3, [3,3,3,1,1,1])