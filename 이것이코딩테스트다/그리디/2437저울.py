# 9시 07분 10시 46분
# 골2
import sys
# n = int(input())
# a = sorted(map(int, input().split()))
n = 3
a = [1,1,2,3,6,7,30]
target = 1
for i in a:
    if target < i:
        break
    target += i
print(target)

