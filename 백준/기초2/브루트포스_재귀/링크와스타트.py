# 20시 28분
# 실1
import itertools as it
import sys
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
a = [sum(i) + sum(j) for i, j in zip(maps, zip(*maps))]
sum1 = sum(a)//2
dif = sys.maxsize
for j in range(1, n//2+1):
    for i in it.combinations(a, n//2):
        dif = min(dif, abs(sum1-sum(i)))
print(dif)