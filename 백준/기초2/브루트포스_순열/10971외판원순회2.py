# 21시 38분 22시 34분
# 실2
import itertools as it
n = int(input())
a = [i for i in range(n)]
map1 = [list(map(int, input().split())) for _ in range(n)]
mini = float('inf')
for arr in it.permutations(a, n):
    sum1 = 0
    excep = 0
    for i in range(len(arr)-1):
        cur = arr[i]
        nex = arr[i+1]
        value = map1[cur][nex]
        if value == 0:
            excep = 1
        sum1 += value
    if excep != 1 and map1[arr[-1]][arr[0]] != 0:
        sum1 += map1[arr[-1]][arr[0]]
        mini = min(mini, sum1)
print(mini)

