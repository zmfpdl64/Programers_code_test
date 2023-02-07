#10시
# 실2
import sys
from itertools import combinations as cb
f = open('startexample.txt', 'r')
input = f.readline
n = int(input())
m = n//2
a = [list(map(int,input().split())) for _ in range(n)]
asum = [sum(i) + sum(j) for i, j in zip(a, zip(*a))]
vsum = sum(asum) // 2
min_v = 1000000000
for i in cb(asum[::-1], m):
    s = abs(vsum - sum(i))
    if min_v > s:
        min_v = s
print(min_v)
