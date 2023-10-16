# 14시 39분 14시 51분
# 실3
# https://www.acmicpc.net/problem/13305

import sys
input = sys.stdin.readline

n = int(input())
lens = list(map(int, input().split()))
op = list(map(int, input().split()))

# 처음 주유소는 무조건 충전해야 한다!!!
answer = op[0] * lens[0]
cur_p = op[0]
# answer  = 10

for i in range(1, len(op) - 1):
    if cur_p > op[i]: # cur_p 2
        cur_p = op[i]
    answer += cur_p * lens[i]
print(answer)

