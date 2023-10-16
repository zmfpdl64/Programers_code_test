# 14시 51분
# 실 3
# https://www.acmicpc.net/problem/18310
import sys

n = int(input())
homes = list(map(int, input().split()))
homes.sort()


result = 0
idx = len(homes) // 2

if len(homes) % 2 == 0:
    result = homes[idx-1]
else:
    result = homes[idx]

print(result)