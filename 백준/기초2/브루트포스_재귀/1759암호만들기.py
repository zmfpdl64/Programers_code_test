# 20시 16분 10시 27분
# 골5
import itertools as it
n, m = map(int, input().split())
a = list(input().split())
a.sort()
b = ['a','e','i','o','u']
for i in it.combinations(a, n):
    count = 0
    for j in i:
        if j in b:
            count += 1
        else:
            pass
    if count>=1 and len(i)-count >= 2:
        print(''.join(i))

