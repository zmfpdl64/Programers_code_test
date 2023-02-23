# 21시 8분 21시 30분
# 실2
import itertools as it
n = int(input())
a = list(map(int, input().split()))
maxi = 0
for arr in it.permutations(a, n):
    sum1 = 0
    for i in range(len(arr)-1):
        sum1 += abs(arr[i] - arr[i+1])
    maxi = max(sum1, maxi)
print(maxi)