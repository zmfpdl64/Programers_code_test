import time
import math
a = list(map(int, input().split()))
a.sort()
answer = list()

st = time.time()

b = math.gcd(a[0], a[1])
c = a[0] * a[1] // b

print( b, c)

ed = time.time()

print(ed - st)